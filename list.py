import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

"""TODO VER CONEXIONES DE BASE DE DATOS!!"""
engine=create_engine('postgresql://postgres:maradona@localhost/')
db= scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("SELECT origin,destination,duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination},{flight.duration} minutes.")


if __name__ == "__main__":
    main()
