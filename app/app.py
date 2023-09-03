from fastapi import FastAPI
import os
import uuid

app = FastAPI()

# Задаем переменные окружения
os.environ['AUTHOR'] = 'Alexander_Pavlov'
os.environ['UUID'] = str(uuid.uuid4())

@app.get('/hostname')
def get_hostname():
    return {'hostname': os.uname().nodename}

@app.get('/author')
def get_author():
    author = os.getenv('AUTHOR')
    if author is not None:
        return {'author': author}
    else:
        return {'error': 'AUTHOR environment variable is not set'}, 500

@app.get('/id')
def get_id():
    uuid_value = os.getenv('UUID')
    if uuid_value is not None:
        return {'uuid': uuid_value}
    else:
        return {'error': 'UUID environment variable is not set'}, 500

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)