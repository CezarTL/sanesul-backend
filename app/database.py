import os
import psycopg2

def get_conn():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise Exception("DATABASE_URL não definida")
    return psycopg2.connect(db_url)
