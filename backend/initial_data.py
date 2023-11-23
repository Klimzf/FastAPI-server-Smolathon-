#!/usr/bin/env python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from main import Place, Icon

data = pd.read_excel('sight.xlsx')

data_colums = ["id", "Название", "Год", "Ширина", "Долгота", "Описание"]

def init() -> None:
    engine = create_engine(
        'sqlite:///work.db',
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()


    db_icon = Icon(path='/icons/map_icon_1.svg')
    db.add(db_icon)
    db.commit()
    db.refresh(db_icon)
    for index, row in data.iterrows():
        db_place = Place(
            name=row[data_colums[1]],
            age=int(row[data_colums[2]]),
            description=row[data_colums[5]],
            latitude=float(row[data_colums[3]]),
            longitude=float(row[data_colums[4]]),
            icon_id=1
        )
        db.add(db_place)
        db.commit()
        db.refresh(db_place)


if __name__ == "__main__":
    print("Add data")
    init()
    print("Complete")