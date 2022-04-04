import uvicorn
from fastapi import FastAPI
import psycopg2

app = FastAPI()


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='bd_django',
                            user='postgres',
                            password='Vlada03042002')
    return conn


@app.get('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT message FROM django_app_hello_message;')
    message = cur.fetchone()
    cur.close()
    conn.close()
    return message


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8020)
