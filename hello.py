from fastapi import FastAPI

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b


app = FastAPI()


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": add_numbers(a, b)}

@app.get("/multiply/{a}/{b}")
def multiply(a: int, b: int):
    return {"result": multiply_numbers(a, b)}

