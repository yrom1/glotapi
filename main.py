"""
curl -X 'GET' \
  'http://127.0.0.1:8000/transpile?sql=SELECT%20EPOCH_MS%281618088028295%29&read=duckdb&write=hive' \
  -H 'accept: application/json'

Should return "SELECT FROM_UNIXTIME(1618088028295 / 1000)"
See https://github.com/tobymao/sqlglot
"""
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlglot import transpile

app = FastAPI()


@app.get("/transpile")
def transpile_(sql: str, read: str, write: str):
    return transpile(sql=sql, read=read, write=write)[0]
    # return {"sql": sql, "read": read, "write": write}


client = TestClient(app)


def test_transpile():
    response = client.get(
        r"/transpile?sql=SELECT%20EPOCH_MS%281618088028295%29&read=duckdb&write=hive"
    )
    print(response)
    assert response.status_code == 200
    assert response.json() == "SELECT FROM_UNIXTIME(1618088028295 / 1000)"
