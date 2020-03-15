import urllib, requests

tele_token = "1035031162:AAHbsYDVpHcxRg0NLJQpgi_VZGyF_gH1gz4"
chat_id = "637286262"

def send_telegram_notif():
	url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
		tele_token, chat_id, urllib.parse.quoteplus('A message has been posted in slack'))

	_ = requests.get(url, timeout=10)