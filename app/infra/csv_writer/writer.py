"""
Essa função escreve um csv ao invés de preencher o banco de dados. Usar padrao de design adapter.
"""

from app.domain.model import Item
from app.logging.logger import getLogger
import csv

logger = getLogger("csv_writer")


def write_csv(filename: str, products: list) -> None:
    try:
      with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = Item.get_field_names()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in products:
          writer.writerow(row)
    except Exception as e:
      logger.error(e)
      raise(e)
        

# with open(csv_file_name, mode='w', newline='') as csv_file:
#     fieldnames = Item.
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)