from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def name():
    return{"hello everyone welcome to github"}