# watch-scope

1. Install dependencies:
```sh
pip install -r requirements.txt
```

2. Copy `settings-sample.py` as `settings.py`
3. Update `settings.py` to configure `TELEGRAM_API_TOKEN` and `CHAT_ID` entries
(You can find `chat_id` with `https://api.telegram.org/bot[YOUR-TOKEN]/getUpdates` after send message to your bot) 
4. run `python3 main.py`