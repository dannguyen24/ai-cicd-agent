from fastapi import FastAPI

# Create your app
app = FastAPI()

# Your first endpoint
@app.get("/")
def hello():
    return {"message": "Hello! Your API is working!"}

# New endpoint that takes a name
@app.get("/greet/{name}")
def greet_person(name: str):
    return {"message": f"Hello {name}! Nice to meet you!"}

# POST endpoint for code generation (fake for now)
@app.post("/generate-code")
def generate_code(request: dict):
    user_prompt = request.get("prompt", "")
    return {
        "your_request": user_prompt,
        "generated_code": f"# Code for: {user_prompt}\nprint('This will be AI-generated later!')"
    }