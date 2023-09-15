from urllib.parse import urljoin
from app.domain.model import Item
from app.logging.logger import getLogger
import re


logger = getLogger("parser.py")


class AdidasParser:
  @staticmethod
  def get_products(data: dict) -> list[dict]:
    raw_products = data["raw"]["itemList"]["items"]
    products = []
    for product in raw_products:
      try:
        title=str(product["altText"]).replace("'", "''")
        discount=round((1 - (product['salePrice'] / product['price'])) * 100)
        
        # a api retorna items indisponiveis, isso garante que há ao menos um tamanho disponível
        is_available = len(product["availableSizes"]) > 1 

        if discount < 40: continue
        if not re.search('tênis', title, re.IGNORECASE): continue
        if not is_available: continue

        item = Item(
          url=urljoin("https://adidas.com.br", product["link"]),
          afiliate_url="",
          title=str(product["altText"]).replace("'", "''"),
          category=product['category'],
          image_url=str(product["image"]["src"]).replace("w_280,h_280", "w_1080,h_1080"),
          price=product["salePrice"],
          previous_price=product["price"],
          discount=discount
        )
        products.append(item.model_dump())
      except Exception as e:
        logger.warning(e)
        continue
    return products
