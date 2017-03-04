from sqlalchemy import (create_engine, Table, Column, Integer, String,
                        MetaData, ForeignKey, insert)
from sqlalchemy.sql import select

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')

    metadata = MetaData()
    metadata.create_all(engine)

    foods = Table('foods', metadata,
                  Column('name', String(50), primary_key=True),
                  Column('calories', String(50)),
                  Column('cuisine', String(50)),
                  Column('is_vegetarian', String(50)),
                  Column('is_gluten_free', String(50))
                  )

    ins = foods.insert().values(
            name="chocolate chip cookie",
            calories="200",
            cuisine="American",
            is_vegetarian="yes",
            is_gluten_free="no"
        )
    print(str(ins))

    conn = engine.connect()

    result = conn.execute(ins)

    s = select([foods])
    result = conn.execute(s)


def initialize_database():
    engine = create_engine('sqlite:///database.db')

    metadata = MetaData()
    metadata.create_all(engine)

    foods = Table('foods', metadata,
                  Column('name', String(50), primary_key=True),
                  Column('calories', String(50)),
                  Column('cuisine', String(50)),
                  Column('is_vegetarian', String(50)),
                  Column('is_gluten_free', String(50))
                  )

    return engine

def insert_new_food(engine, name, calories, cuisine, is_vegetarian, is_gluten_free):
    metadata = MetaData()
    metadata.create_all(engine)

    foods = Table('foods', metadata,
                  Column('name', String(50), primary_key=True),
                  Column('calories', String(50)),
                  Column('cuisine', String(50)),
                  Column('is_vegetarian', String(50)),
                  Column('is_gluten_free', String(50))
                  )

    ins = foods.insert().values(
        name=name,
        calories=calories,
        cuisine=cuisine,
        is_vegetarian=is_vegetarian,
        is_gluten_free=is_gluten_free
    )
    conn = engine.connect()
    conn.execute(ins)


def get_favorite_food(engine, favorite_food):
    metadata = MetaData()
    metadata.create_all(engine)

    foods = Table('foods', metadata,
                  Column('name', String(50), primary_key=True),
                  Column('calories', String(50)),
                  Column('cuisine', String(50)),
                  Column('is_vegetarian', String(50)),
                  Column('is_gluten_free', String(50))
                  )

    conn = engine.connect()
    s = select([foods]).where(foods.c.name == favorite_food)
    results = conn.execute(s)
    return results
