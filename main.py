
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from auth import verify_token
from gemini_client import generate_response
from system_optimizer import get_system_info
from exception_handlers import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from logger import logger

app = FastAPI()
app.add_exception_handler(RequestValidationError, validation_exception_handler)


class CommandRequest(BaseModel):
    input: str

class ExplainRequest(BaseModel):
    command: str


@app.post("/translate")
async def translate_command(data: CommandRequest, auth: bool = Depends(verify_token)):
    logger.info(f"Translate input: {data.input}")
    prompt = f"Translate this natural language description into a single, safe, and common Linux bash command. Only return the command itself, with no explanation or extra text.\n\nDescription: {data.input}"
    bash_command = await generate_response(prompt)
    logger.info(f"Bash command: {bash_command}")
    cleaned_command = bash_command.strip().replace("`", "")
    return {"bash_command": cleaned_command}


@app.post("/explain")
async def explain_command(data: ExplainRequest, auth: bool = Depends(verify_token)):
    logger.info(f"Explain input: {data.command}")

    prompt = f"""
Analyze the following Linux command and provide a concise, professional explanation.

Your response must follow this exact format:
**Summary:** A single sentence explaining the command's primary function.
**Breakdown:**
- `component1`: Brief explanation of the first part.
- `component2`: Brief explanation of the second part.
- etc.

Command to analyze: `{data.command}`
"""

    explanation = await generate_response(prompt)

    cleaned_explanation = (
        explanation.replace("**", "").replace("*", "").replace("- ", "")
    )

    logger.info(f"Cleaned Explanation: {cleaned_explanation}")
    return {"explanation": cleaned_explanation.strip()}


@app.get("/optimize")
async def optimize_system(auth: bool = Depends(verify_token)):
    logger.info("Optimize request received")
    sys_info = get_system_info()
    summary = (
        f"CPU Load: {sys_info.get('cpu_load')}\n"
        f"RAM Usage: {sys_info.get('ram_usage')}\n"
        f"Disk Usage: {sys_info.get('disk_usage')}\n"
        f"Active Services: {sys_info.get('active_services')[:500]}"
    )
    logger.info(f"System Snapshot: {summary[:300]}...")
    prompt = f"Given the following system snapshot, suggest 3-5 safe, actionable performance tweaks for a Linux server. Present them as a bulleted list. Focus on beginner-friendly advice.\n\n{summary}"
    suggestions = await generate_response(prompt)
    return {"optimizations": suggestions}
