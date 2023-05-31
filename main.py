# import FastAPI
from fastapi import FastAPI
# import module from FastAPI for redirecting
from fastapi.responses import RedirectResponse

# start FastAPI app
app = FastAPI()

# define root controller that redirects to /docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# define controller that accepts name as a parameter and returns a {"assistant":"Here's my answer, {name}."} 
@app.get("/assistant/{name}")
async def assistant(name: str):
    return {"assistant": f"Here's my answer, {name}."}

# define a post controller that accepts name as a key and returns a {"assistant":"Here's my answer, {name}."}
@app.post("/assistant")
async def assistant(name: str):
    return {"assistant": f"Here's my answer, {name}."}
    