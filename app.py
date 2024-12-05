from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Define the request body schema
class CommandRequest(BaseModel):
    command: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the command runner API"}

@app.post("/run-command/")
def run_command(request: CommandRequest):
    try:
        # Run the shell command and capture output
        result = subprocess.check_output(request.command, shell=True, text=True, stderr=subprocess.STDOUT)
        return {"output": result}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Command failed: {e.output}")
