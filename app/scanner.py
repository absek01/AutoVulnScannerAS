import requests  # Import the requests library to make HTTP requests
import base64  # Import the base64 library to encode the URL

# Define the API key for VirusTotal and the URL endpoint
API_KEY = '23bad8c89f9b88355eccedf72a47b349d3e722eeee22eb23d417e579a9a68c49'
VT_URL = 'https://www.virustotal.com/api/v3/urls/'

# Dictionary to describe different types of vulnerabilities
VULNERABILITY_DESCRIPTIONS = {
    'phishing': 'Phishing is an attack where the attacker disguises as a trusted entity to steal sensitive information such as login credentials and credit card numbers.',
    'malware': 'Malware is any software intentionally designed to cause damage to a computer, server, client, or computer network. It can steal, encrypt, or delete sensitive data.',
    'suspicious': 'A suspicious detection means that the URL or file exhibits behavior that is not typical of benign software or websites. This could potentially indicate a threat.',
    'undetected': 'Undetected means that no malicious activity or threats were found by the scanning engines.',
    'sql_injection': 'SQL Injection is a code injection technique that might destroy your database. It is one of the most common web hacking techniques.',
    'xss': 'Cross-Site Scripting (XSS) is a type of injection where malicious scripts are injected into otherwise benign and trusted websites.'
}

# Function to scan a URL for vulnerabilities
def scan_url(url):
    # Convert the URL to a format suitable for VirusTotal API
    url_id = get_url_id(url)
    # Set the headers including the API key for authorization
    headers = {
        'x-apikey': API_KEY,
        'Accept': 'application/json'
    }
    # Make a GET request to VirusTotal API with the encoded URL
    response = requests.get(f'{VT_URL}{url_id}', headers=headers)
    # Convert the response to JSON format
    result = response.json()

    # Iterate through the scan results from different analysis engines
    for engine, analysis in result['data']['attributes']['last_analysis_results'].items():
        # Check if the analysis category is in the vulnerability descriptions dictionary
        if analysis['category'] in VULNERABILITY_DESCRIPTIONS:
            # Add the description to the analysis result
            analysis['description'] = VULNERABILITY_DESCRIPTIONS[analysis['category']]
        else:
            # If no description is available, indicate that
            analysis['description'] = 'No detailed description available.'

    # Return the final result with descriptions added
    return result

# Function to encode the URL for use with VirusTotal API
def get_url_id(url):
    # Encode the URL in a base64 format suitable for VirusTotal API and remove padding
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')
    return url_id
