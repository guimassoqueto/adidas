from app.app import get_urls, application
from app.settings import MAX_CONCURRENCY
from app.logging.logger import getLogger
from asyncio import create_task, gather, run, Semaphore


logger = getLogger("main")
CONCURRENCY_LIMIT = Semaphore(MAX_CONCURRENCY)


async def main(concurrency_limit: Semaphore) -> None:
  try:
    urls = await get_urls()
    tasks = []
    for url in urls:
        task = create_task(application(url, concurrency_limit=concurrency_limit))
        tasks.append(task)
    result = await gather(*tasks)
    return result
  except Exception as e:
    raise e


if __name__ == "__main__":
  logger.info("Inializing application...")
  try:
    result = run(main(CONCURRENCY_LIMIT))
    if result: logger.info("Completed.")
  except Exception as e:
    logger.error(e, stack_info=True)
