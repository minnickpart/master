from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the command runner API"}

@app.post("/run-command/")
def run_command(command: str):
    try:
        # Run the shell command and capture output
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return {"output": result}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Command failed: {e.output}")
