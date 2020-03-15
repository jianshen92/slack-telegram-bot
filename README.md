# slack-telegram-bot

Deploys a slackbot on Heroku that listens to mentions/messages in Slack Channels and send some messages to Telegram Group Chat.   

Tested on Python 3.7

## Getting started
#### Setup your slackbot
Follow this [guide](https://github.com/slackapi/python-slackclient/tree/master/tutorial).

#### Get Telegram Token
Follow this [gist](https://gist.github.com/dlaptev/7f1512ee80b7e511b0435d3ba95d88cc).

#### Environment Variables
Variable Name | Description 
--- | ---
`SLACK_TOKEN` | Slack's Bot Oath Token
`SLACK_SIGNING_TOKEN` | Signing Secret
`TELEGRAM_TOKEN` | Telegram Bot Token
`TELEGRAM_CHAT_ID`| Telegram Chat Group ID

### Run Locally
Install dependencies.
```
pip install -r requirements.txt
```

Run Flask app
```
python app.py
```

Mention your bot in your channels, your telegram bo

### Deploy to heroku
Setup with this very simple and sweet [guide](https://stackabuse.com/deploying-a-flask-application-to-heroku/).

And just deploy with
```
git push heroku master
```

## Author
* [@szeshen](https://github.com/szeshen)
* Myself
