# Python libraries that we need to import for our bot
from flask import Flask, request
from pymessenger2.bot import Bot
from PIL import Image
import requests
from io import BytesIO
import BicubicEnhance

app = Flask(__name__)
ACCESS_TOKEN = 'ACCESS_TOKEN'
VERIFY_TOKEN = '4tynswpmkn8s0'
bot = Bot("EAAC1O1Kjh9IBAJQkodbIG8oKgBg9ZChQBWIXrZAM9AZBGYEgmwHpDgCMCMdmsxUR1arISzjNDxQ6J8IQCLJjxl4XMXlQ2OhUomZCrcZBZC5"
          "aEeAwtvHn35uyZChVLmO87zsCDLKoxpdzBDoywH5ZAoO61xlmtWAZBaP4SNmNdjhE62WZCmunrv0FoM")


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo, video, or any other non-text item
                    if message['message'].get('attachments'):
                        image_URL =  message['message']['attachments'][0]['payload']['url']
                        response = requests.get(image_URL)
                        img = Image.open(BytesIO(response.content))
                        img.show()
                        output = BicubicEnhance.bicubic(img)
                        output.show()
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def get_message():
    return "LISTENING"


# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run()
