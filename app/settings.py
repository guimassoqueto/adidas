from dotenv import load_dotenv
from os import getenv
load_dotenv()


POSTGRES_PORT = getenv("POSTGRES_PORT") or 5432
POSTGRES_DB = getenv("POSTGRES_DB") or "postgres"
POSTGRES_USER = getenv("POSTGRES_USER") or "postgres"
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD") or "password"
POSTGRES_HOST = getenv("POSTGRES_HOST") or "127.0.0.1"
TABLE_NAME = getenv("TABLE_NAME", "sports")
ADIDAS_API = getenv("ADIDAS_API", "")
MAX_CONCURRENCY = int(getenv("MAX_CONCURRENCY", 8))
