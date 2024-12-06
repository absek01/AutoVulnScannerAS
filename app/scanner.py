import requests
import subprocess
import time

# Ensure ZAP is running
def start_zap():
    try:
        subprocess.Popen(['zap.sh', '-daemon'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(10)  # Wait for ZAP to start
    except Exception as e:
        print(f"Error starting ZAP: {e}")

ZAP_URL = 'http://localhost:8080'  # URL where ZAP API is available

def scan_url(url):
    start_zap()  # Ensure ZAP is running
    start_scan(url)
    results = {
        'sql_injection': check_sql_injection(),
        'xss': check_xss()
    }
    return results

def start_scan(url):
    scan_url = f'{ZAP_URL}/JSON/ascan/action/scan/?url={url}'
    response = requests.get(scan_url)
    return response.json()

def check_sql_injection():
    issues = get_alerts()
    for issue in issues:
        if 'SQL Injection' in issue['alert']:
            return True
    return False

def check_xss():
    issues = get_alerts()
    for issue in issues:
        if 'Cross Site Scripting' in issue['alert']:
            return True
    return False

def get_alerts():
    alerts_url = f'{ZAP_URL}/JSON/core/view/alerts/'
    response = requests.get(alerts_url)
    return response.json().get('alerts', [])
