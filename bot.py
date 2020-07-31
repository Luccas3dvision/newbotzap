#import com pip flask request twilio
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


#documentacao do twilio tem o start 
#flask requests
app = Flask(__name__)
#config do  ngrok  
#[ip]/bot no Twilio  https://www.twilio.com/console/sms/whatsapp/sandbox  
# rota para receber o request
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
@app.route('/bot', methods=['POST'])
#toda vez que houver um request responde com a funcao
#essa funcao voce econtra na documentacao do https://www.twilio.com/docs/sms/quickstart/python
def bot():
    #pega msg armazena o que foi escrito 
    resp = MessagingResponse()
    #cria uma resposta
    msg = resp.message()
    #formata a resposta
    msg.body('Responda, funcionando')
    #e retorna
    return str(resp)


#mantem ativo o script
if __name__== '__main__':
    app.run()
