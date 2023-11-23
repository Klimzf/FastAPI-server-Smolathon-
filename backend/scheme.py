from pydantic import BaseModel
from typing import Optional


class IconOut(BaseModel):
    path: str

    class Config:
        orm_mode = True


class PlaceOut(BaseModel):
    id: int
    name: str
    age: int
    description: str
    latitude: float
    longitude: float
    icon: Optional[IconOut] = None

    class Config:
        orm_mode = True