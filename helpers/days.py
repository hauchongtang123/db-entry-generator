import datetime
import random


def generate_random_days() -> list:
    num_days = random.randint(1, 5)
    whitelist = random.sample(range(7), k=num_days)
    return whitelist


def generate_sql_datetime(idx: int) -> str:
    # Define the time to add per index
    years_per_index = datetime.timedelta(days=365)
    time_per_index = datetime.timedelta(hours=6)
    current_datetime = datetime.datetime.now() - years_per_index
    current_datetime += time_per_index * idx
    sql_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return sql_datetime
