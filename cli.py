
import argparse
import requests

API_URL = "https://terminalai-f9e6f5821023.herokuapp.com/"

TOKEN = "tA-s3cr3t-p@ssw0rd-f0r-my-@pi-4815162342"

def call_api(endpoint, payload=None):
    headers = {"X-Token": TOKEN}
    url = f"{API_URL}/{endpoint}"
    
    try:
        response = requests.post(url, json=payload, headers=headers) if payload else requests.get(url, headers=headers)
        response.raise_for_status() 
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


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