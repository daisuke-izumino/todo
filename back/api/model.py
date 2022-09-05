from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.schema import FetchedValue
from db import Base
from db import ENGINE

# テーブル定義
class TaskTable(Base):
    __tablename__ = 'task'
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    text = Column(Text(1024), nullable=False)
    created_at = Column(TIMESTAMP, FetchedValue())
    updated_at = Column(TIMESTAMP, FetchedValue())

def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()