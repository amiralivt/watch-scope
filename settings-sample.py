BASE_DATA_URL = 'https://github.com/Osb0rn3/bugbounty-targets/tree/main/programs'

PLATFORMS = [
    {
        "name": "hackerone",
        "scope": "asset_identifier",
        "type": "asset_type",
        "valid_types": ['URL', 'CIDR'],
        "url": f"{BASE_DATA_URL}hackerone.json",
    },
    {
        "name": "bugcrowd",
        "valid_types": ['website', 'api'],
        "url": f"{BASE_DATA_URL}bugcrowd.json",
    },
    {
        "name": "intigriti",
        "scope": "endpoint",
        "valid_types": ['url', 'iprange'],
        "url": f"{BASE_DATA_URL}intigriti.json",
    },
    {
        "name": "yeswehack",
        "valid_types": ['web-application', 'ip-address', 'api'],
        "url": f"{BASE_DATA_URL}yeswehack.json",
    },
]

TELEGRAM_API_TOKEN = 'YOUR-TOKEN'
TELEGRAM_SEND_URL = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
CHAT_ID = 0

SEND_NO_CHANGES = True
