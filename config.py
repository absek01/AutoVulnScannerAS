import os


class Config:
    # Basic Configurations
    DEBUG = True  # Enable/Disable debug mode
    TESTING = False  # Enable/Disable testing mode

    # VirusTotal API Key
    VT_API_KEY = os.getenv('VT_API_KEY', '23bad8c89f9b88355eccedf72a47b349d3e722eeee22eb23d417e579a9a68c49')

