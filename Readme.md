# fastapi-web-tryout

## Usage
### Local
- python
- git

### Use Docker
- docker
- git


## How To Use
### Local
1. Install Third Party Package
```
pip install -r requirements.txt
```
2. Start application use uvicorn.
```
cd app
uvicorn main:app --reload --port 8080 # Access http://localhost:8080/
```

### Docker
1. Build container
```
docker compose build
```
2. Start container
```
docker compose up -d # Access http://localhost:8080/
```