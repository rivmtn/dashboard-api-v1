import os

from dotenv import load_dotenv

load_dotenv()

# JWT
ACCESS_TOKEN_EXPIRE_HOURS = 24
ACCESS_TOKEN_ALGORITHM = os.getenv("ACCESS_TOKEN_ALGORITHM")
# openssl rand -hex 64 터미널 실행 후 나온 결과를 아래에 붙여넣기
ACCESS_TOKEN_SECRET_KEY = os.getenv("ACCESS_TOKEN_SECRET_KEY")

# DATABASE
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = "3306"
DB_DATABASE = os.getenv("DB_DATABASE")
DB_CHARSET = "utf8mb4"
DB_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}"
