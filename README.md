# math-svc

tiny micro-service that computes three classic math operations, stores every request in SQLite, and ships with Docker 

> **Project developed by:**  
> Darius Fratila  
> Octavian Paul Ilies  
> Adina Denisa Horj
---

## quick-start (local)

```bash
# 1. create & activate venv
python -m venv .venv && source .venv/bin/activate

# 2. install deps
pip install -r requirements.txt

# 3. launch api
PYTHONPATH=src python src/interface/api_app.py

## sample calls 
# hello
curl http://localhost:5000/

# 2^10
curl -X POST http://localhost:5000/calc \
     -H "content-type: application/json" \
     -d '{"op":"pow","args":[2,10]}'

# list all requests
curl http://localhost:5000/logs

# fetch one request
curl http://localhost:5000/logs/3

# delete a request
curl -X DELETE http://localhost:5000/logs/3

## quick-start (docker)

docker build -t mathsvc .
docker run --rm -p 5000:5000 mathsvc

## test & lint

pytest        
flake8 .     

## project layout
src/
|-- interface/         # api_app.py
|-- math_operations/   # pow, fib, fact + factory
|-- database_infra/    # sqlite repo, factory
|-- logs/              # request_entry model
|-- tests/             # pytest suite
