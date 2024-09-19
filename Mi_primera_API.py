from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/inicio")
def read_root():
    return {"Hello": "World"}

@app.get("/parametros/{nombre}")
def get_parametros(nombre):
    return {
        "Nombre" : nombre
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/incremento/{numero}")
def get_incremento(numero:int):
    numero = numero + 1
    return {
        "Numero" : numero
    }