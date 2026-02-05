from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Login123@localhost:3306/blog"
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://root:Login123@localhost:5432/blog"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)


'''{"check_same_thread" only add for sql lite'''
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
