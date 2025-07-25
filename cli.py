import argparse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://terminalai-f9e6f5821023.herokuapp.com/"  # Replace with your live Render URL
TOKEN = os.getenv("GOOGLE_API_KEY")

def call_api(endpoint, payload=None):
    headers = {"X-Token": TOKEN} if TOKEN else {}
    url = f"{API_URL}/{endpoint}"
    response = requests.post(url, json=payload, headers=headers) if payload else requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")

parser = argparse.ArgumentParser(description="TerminalGPT CLI")
parser.add_argument("mode", choices=["translate", "explain", "optimize"])
parser.add_argument("input", nargs="?", help="Command or description")

args = parser.parse_args()

if args.mode == "translate":
    if not args.input:
        print("Please provide natural language input.")
    else:
        call_api("translate", {"input": args.input})
elif args.mode == "explain":
    if not args.input:
        print("Please provide a bash command to explain.")
    else:
        call_api("explain", {"command": args.input})
elif args.mode == "optimize":
    call_api("optimize")
