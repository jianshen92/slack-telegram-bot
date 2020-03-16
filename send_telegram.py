import urllib, requests
import os

tele_token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

def send_telegram_notif():
	url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
		tele_token, chat_id, urllib.parse.quote_plus('An important message has been posted in slack! Please check :)'))

	_ = requests.get(url, timeout=10)