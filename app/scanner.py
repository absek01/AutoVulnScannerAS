import requests
import base64

API_KEY = '23bad8c89f9b88355eccedf72a47b349d3e722eeee22eb23d417e579a9a68c49'
VT_URL = 'https://www.virustotal.com/api/v3/urls/'

VULNERABILITY_DESCRIPTIONS = {
    'phishing': 'Phishing is an attack where the attacker disguises as a trusted entity to steal sensitive information such as login credentials and credit card numbers.',
    'malware': 'Malware is any software intentionally designed to cause damage to a computer, server, client, or computer network. It can steal, encrypt, or delete sensitive data.',
    'suspicious': 'A suspicious detection means that the URL or file exhibits behavior that is not typical of benign software or websites. This could potentially indicate a threat.',
    'undetected': 'Undetected means that no malicious activity or threats were found by the scanning engines.',
    'sql_injection': 'SQL Injection is a code injection technique that might destroy your database. It is one of the most common web hacking techniques.',
    'xss': 'Cross-Site Scripting (XSS) is a type of injection where malicious scripts are injected into otherwise benign and trusted websites.'
}


def scan_url(url):
    url_id = get_url_id(url)
    headers = {
        'x-apikey': API_KEY,
        'Accept': 'application/json'
    }
    response = requests.get(f'{VT_URL}{url_id}', headers=headers)
    result = response.json()

    for engine, analysis in result['data']['attributes']['last_analysis_results'].items():
        if analysis['category'] in VULNERABILITY_DESCRIPTIONS:
            analysis['description'] = VULNERABILITY_DESCRIPTIONS[analysis['category']]
        else:
            analysis['description'] = 'No detailed description available.'

    return result


def get_url_id(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')
    return url_id
