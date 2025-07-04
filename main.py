from fastapi import FastApi
app=FastApi()
@app.get("/")
def name():
    return{"hello everyone welcome to github"}