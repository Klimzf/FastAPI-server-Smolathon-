import logging
from typing import Any, List

from models import Place, Icon
import uvicorn
from fastapi import Depends, FastAPI
from scheme import PlaceOut
from db import get_db
from filter import PlaceFilter
from sqlalchemy import event, select
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware

from fastapi_filter import FilterDepends


logger = logging.getLogger("uvicorn")


@event.listens_for(Engine, "connect")
def _set_sqlite_case_sensitive_pragma(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA case_sensitive_like=ON;")
    cursor.close()


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/places", response_model=List[PlaceOut])
async def get_addresses(
    place_filter: PlaceFilter = FilterDepends(PlaceFilter),
    db: AsyncSession = Depends(get_db),
) -> Any:
    query = select(Place).join(Icon)
    query = place_filter.filter(query)
    query = place_filter.sort(query)
    result = await db.execute(query)
    return result.scalars().all()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)