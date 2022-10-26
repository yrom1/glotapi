set -eou pipefail
py -m pip install -r requirements.txt
uvicorn main:app --reload

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/items/5?q=somequery
