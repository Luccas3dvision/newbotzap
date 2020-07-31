from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'fofos' in incoming_msg:
        # return a fofos para projetos futuro
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            fofos = f'{data["content"]} ({data["author"]})'
        else:
            fofos = 'Para ver gatos.'
        msg.body(fofos)
        responded = True
    if 'gato' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('Digitando a palavra gato eu te mando uma foto.')
    return str(resp)


if __name__ == '__main__':
    app.run()