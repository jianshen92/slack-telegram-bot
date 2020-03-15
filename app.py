from flask import Flask
from slackeventsapi import SlackEventAdapter

from slack import WebClient

from send_telegram import send_telegram_notif

import os

SLACK_TOKEN = os.environ['SLACK_TOKEN']
slack_client = WebClient(SLACK_TOKEN)

# This `app` represents your existing Flask app
app = Flask(__name__)


# An example of one of your Flask app's routes
@app.route("/")
def hello():
	return "Hello theree!"

# Bind the Events API route to your existing Flask app by passing the server
# instance as the last param, or with `server=app`.
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_TOKEN'], "/slack/events", app)

# Create an event listener for "reaction_added" events and print the emoji name
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
	emoji = event_data["event"]["reaction"]

	slack_client.chat_postMessage(
		channel="bots-talk",
		text=f"{emoji}"
	)

@slack_events_adapter.on("message")
def message_channel(event_data):
	# print(json.dumps(event_data))
	if "bot_id" in event_data["event"]:
		return
	#
	# import pdb
	# pdb.set_trace()
	text = event_data["event"]["text"]
	print(text)

	slack_client.chat_postMessage(
		channel="bots-talk",
		text=f"{text}"
	)


@slack_events_adapter.on("app_mention")
def mention_me(event_data):
	print("sup")
	send_telegram_notif()

# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)