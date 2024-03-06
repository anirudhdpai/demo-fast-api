from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}

@app.post('/')
async def root():
    return {'message': 'hello world'}

@app.put('/')
async def root():
    return {'message': 'hello world'}

