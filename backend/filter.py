from fastapi_filter.contrib.sqlalchemy import Filter
from models import Place
from typing import List, Optional


class PlaceFilter(Filter):
    age__lte: Optional[int] = None

    order_by: List[int] = ["age"]

    class Constants(Filter.Constants):
        model = Place
