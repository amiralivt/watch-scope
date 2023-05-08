BASE_DATA_URL = 'https://github.com/Osb0rn3/bugbounty-targets/raw/main/programs/'

PLATFORMS = [
    {
        "name": "hackerone",
        "valid_types": ['URL', 'CIDR'],
        "url": f"{BASE_DATA_URL}hackerone.json",
        "base_url": "https://hackerone.com/",
    },
    {
        "name": "bugcrowd",
        "valid_types": ['website', 'api'],
        "url": f"{BASE_DATA_URL}bugcrowd.json",
        "base_url": "https://bugcrowd.com/",
    },
    {
        "name": "intigriti",
        "valid_types": [1, 4],
        "url": f"{BASE_DATA_URL}intigriti.json",
        "base_url": "https://app.intigriti.com/programs/",
    },
    {
        "name": "yeswehack",
        "valid_types": ['web-application', 'ip-address', 'api'],
        "url": f"{BASE_DATA_URL}yeswehack.json",
        "base_url": "https://yeswehack.com/programs/",
    },
]

TELEGRAM_API_TOKEN = 'YOUR-TOKEN'
TELEGRAM_SEND_URL = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
CHAT_ID = 0

SEND_NO_CHANGES = True
