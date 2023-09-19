from asyncio import Semaphore
from app.handlers.parser import AdidasParser
from app.infra.aiohttp.aioretry import AioHttpRetry
from app.infra.psycopg.postgres import insert_products
from app.settings import ADIDAS_API
import math


async def get_urls() -> int:
  data = await AioHttpRetry.get_json(ADIDAS_API)
  total_items = data["raw"]["itemList"]["count"]
  items_per_url = data["raw"]["itemList"]["viewSize"]
  total_pages = math.ceil(total_items/items_per_url)
  urls = [f"{ADIDAS_API}&start={i * items_per_url}" for i in range(1, total_pages)]
  return urls


async def application(url, concurrency_limit: Semaphore) -> None:
  async with concurrency_limit:
    data = await AioHttpRetry.get_json(url)
    products = AdidasParser.get_products(data)
    insert_products("items.csv", products)
  