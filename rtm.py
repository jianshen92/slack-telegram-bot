from slack import RTMClient

import os

@RTMClient.run_on(event="message")
def say_hello(**payload):
	data = payload['data']
	web_client = payload['web_client']

	if "subtype" in data:
		if data["subtype"] == "bot_message":
			return

		return

	channel_id = data['channel']
	user = data['user']

	web_client.chat_postMessage(
	  channel=channel_id,
	  text=f"Send this message '{data['text']}' from <@{user}> to Telegram !",
	)

slack_token = os.environ['SLACK_TOKEN']
rtm_client = RTMClient(token=slack_token)
rtm_client.start()