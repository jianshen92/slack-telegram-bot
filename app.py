from flask import Flask
from slackeventsapi import SlackEventAdapter

from slack import WebClient

SLACK_TOKEN = "xoxb-990892714049-1001003062405-5nj4I8iE7GvOkZiTBzKtBXGY"
slack_client = WebClient(SLACK_TOKEN)

# This `app` represents your existing Flask app
app = Flask(__name__)


# An example of one of your Flask app's routes
@app.route("/")
def hello():
	return "Hello theree!"

# Bind the Events API route to your existing Flask app by passing the server
# instance as the last param, or with `server=app`.
slack_events_adapter = SlackEventAdapter("20b6efc3fa89ef0ea5bcf455b6f7bb2b", "/slack/events", app)

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


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)