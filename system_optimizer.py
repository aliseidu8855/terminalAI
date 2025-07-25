import subprocess

def get_system_info():
    info = {}
    try:
        info["cpu_load"] = subprocess.getoutput("uptime")
        info["ram_usage"] = subprocess.getoutput("free -h")
        info["disk_usage"] = subprocess.getoutput("df -h /")
        info["active_services"] = subprocess.getoutput("systemctl list-units --type=service --state=running")
    except Exception as e:
        info["error"] = str(e)
    return info
