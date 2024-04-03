from datetime import datetime
from typing import Callable

from pytz import timezone

current_time: Callable[[], str] = \
    lambda: datetime.now(timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")

current_date: Callable[[], str] = \
    lambda: datetime.now(timezone("Asia/Seoul")).strftime("%Y-%m-%d")

time_to_date: Callable[[datetime], str] = \
    lambda time: time.strftime("%Y-%m-%d")
