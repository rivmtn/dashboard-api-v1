import random
from datetime import datetime, timedelta

import pymysql

from app.util.config import DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_CHARSET


# 더미 데이터 생성 및 삽입 함수
def insert_dummy_data(n=1000):
    # 데이터베이스 연결
    conn = pymysql.connect(host=DB_HOSTNAME,
                           user=DB_USERNAME,
                           password=DB_PASSWORD,
                           db=DB_DATABASE,
                           charset=DB_CHARSET)
    try:
        with conn.cursor() as cursor:
            # 마지막 날짜 설정
            end_date = datetime(2024, 4, 3)

            for _ in range(n):
                # 날짜 계산
                day = end_date - timedelta(days=_)
                day_int = int(day.strftime('%Y%m%d'))

                # 더미 데이터 생성
                imp = random.randint(1000, 10000)
                click = random.randint(1, imp)
                order_cnt = random.randint(1, click)
                cancel_cnt = random.randint(1, order_cnt)
                sale = random.randint(100000, 1000000)
                revenue = int(sale * 0.9)

                # SQL 쿼리
                sql = """
                INSERT INTO reports (day, imp, click, order_cnt, cancel_cnt, sale, revenue)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (day_int, imp, click, order_cnt, cancel_cnt, sale, revenue))

        # 변경사항 커밋
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    # 더미 데이터 삽입 실행
    insert_dummy_data()
