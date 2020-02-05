from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class Connection:
    def __init__(self):
        host = "remotemysql.com"
        database = "FN9HPlCnS4"
        user = "FN9HPlCnS4"
        passwd = "7JvI9lqKdJ"

        connectStr = f"mysql://{user}:{passwd}@{host}/{database}"

        engine = create_engine(connectStr, echo=True)
        Session = sessionmaker(bind=engine)
        self.session= Session()
