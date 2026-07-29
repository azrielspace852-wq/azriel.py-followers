import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TIKTOK_USERNAME = os.getenv('TIKTOK_USERNAME', 'azriel.py')
    PORT = int(os.getenv('PORT', 5000))
    DEBUG = True
    
    # Data profil
    PROFILE_NAME = "Azriel.py"
    EMAIL = "azrielspace852@gmail.com"
    
    # Links
    LINKS = [
        {"name": "Axion Neuralis", "url": "https://axion-neuralis.pages.dev/"},
        {"name": "Azriel Space", "url": "https://azriel-space.pages.dev/"},
        {"name": "TikTok", "url": "https://vm.tiktok.com/ZS9h1CJq2UuVE-R4juq/"}
    ]