import requests
import base64

API_KEY = '23bad8c89f9b88355eccedf72a47b349d3e722eeee22eb23d417e579a9a68c49'
VT_URL = 'https://www.virustotal.com/api/v3/urls/'

def scan_url(url):
    url_id = get_url_id(url)
    headers = {
        'x-apikey': API_KEY,
        'Accept': 'application/json'
    }
    response = requests.get(f'{VT_URL}{url_id}', headers=headers)
    return response.json()

def get_url_id(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')
    return url_id
