from sqlalchemy.orm import declarative_base, Mapped, relationship
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey

Base = declarative_base()


class Icon(Base):
    __tablename__ = "icon"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, nullable=False)


class Place(Base):
    __tablename__ = "place"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    icon_id = Column(Integer, ForeignKey("icon.id"), name='icon', nullable=True)
    icon: Mapped[Icon] = relationship(Icon, backref="icons", lazy="joined")

