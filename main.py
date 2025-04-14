import uvicorn

if __name__ == "__main__":
    #Run the app object found in app/main.py
    uvicorn.run("app.main:app", reload=True)