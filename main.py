#!/usr/bin/python3

import os
import requests
import json
from settings import PLATFORMS, TELEGRAM_SEND_URL, CHAT_ID, SEND_NO_CHANGES


def escape_text(text):
    chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in chars:
        text = text.replace(char, f"\\{char}")
    
    return text


def send_notif(text):
    data = {
        'chat_id': CHAT_ID,
        'parse_mode': 'MarkdownV2',
        'text': text,
    }
    requests.post(TELEGRAM_SEND_URL, data=data)


DB_PATH = os.path.dirname(__file__)
DB_FILE = os.path.join(DB_PATH, 'db.json')
first_pull = True
db = {}
if os.path.isfile(DB_FILE):
    first_pull = False
    with open(DB_FILE, encoding='utf8') as f:
        db = json.load(f)

newData = {}
changes = {}
for platform in PLATFORMS:
    data_url = platform['url']
    platform_name = platform.get('name')
    valid_types = platform.get('valid_types')
    base_url = platform.get('base_url')

    response = requests.get(data_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"[+] Load {len(data)} targets from {platform_name}")
        for item in data:
            if platform_name == 'hackerone':
                name = item.get('attributes').get('name')
                url = f"{base_url}{item.get('attributes').get('handle')}/"
                scopes = item.get('relationships').get('structured_scopes').get('data')
                in_scope = [scope.get('attributes').get('asset_identifier') for scope in scopes
                            if scope.get('attributes').get('eligible_for_submission') == True and scope.get('attributes').get('asset_type') in valid_types]
                
            elif platform_name == 'bugcrowd':
                name = item.get('name')
                url = f"{base_url}{item.get('program_url')}"
                scopes = item.get('target_groups')
                in_scope = [target.get('name') for scope in scopes for target in scope.get('targets') if scope.get('in_scope') == True and target.get('category') in valid_types]
                
            elif platform_name == 'intigriti':
                name = item.get('name')
                url = f"{base_url}{item.get('companyHandle')}/{item.get('handle')}/"
                scopes = item.get('domains')
                in_scope = [scope.get('endpoint') for scope in scopes if scope.get('type') in valid_types]
            
            elif platform_name == 'yeswehack':
                name = item.get('title')
                url = f"{base_url}{item.get('slug')}"
                scopes = item.get('scopes')
                in_scope = [scope.get('scope') for scope in scopes if scope.get('scope_type') in valid_types]
            
            else:
                break

            if name in newData.keys():
                newData[name] = {
                    'platform': newData.get(name).get('platform') + ',' + platform_name,
                    'url': newData.get(name).get('url') + ',' + url,
                    'in_scope': list(set(newData.get(name).get('in_scope') + in_scope)),
                }
            else:
                newData[name] = {'platform': platform_name, 'url': url, 'in_scope': in_scope}

            if not first_pull:
                if name in db.keys():
                    old_scope = db.get(name).get('in_scope')
                    change_scope = [x for x in in_scope if x not in old_scope]
                else:
                    change_scope = in_scope

                if len(change_scope) > 0:
                    changes[name] = {'platform': platform_name, 'url': url, 'in_scope': change_scope}

    else:
        print(f"[!] Failed to load targets from {platform_name}")


if first_pull:
    print(f"[+] DB initial with {len(newData)} targets")
elif len(changes) > 0:
    for item in changes:
        text = f"*{item}*\r\n"
        text += "\r\n".join([f"[More info]({escape_text(x)})" for x in changes.get(item).get('url').split(',')])
        text += "\r\nScope:\r\n"
        text += "```\r\n"
        text += escape_text("\r\n".join(changes.get(item).get('in_scope')))
        text += "```\r\n"
        send_notif(text)
else:
    if SEND_NO_CHANGES:
        text = 'No changes for targets or scopes'
        send_notif(text)


with open(DB_FILE, 'w', encoding='utf8') as f:
    f.write(json.dumps(newData, ensure_ascii=False, indent=2))