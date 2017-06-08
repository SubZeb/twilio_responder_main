# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from twilio import twiml
import randGen

app = Flask(__name__)


def command_parser(body):
    body = body.split(' ')
    holder = []
    for i in body:
        holder.append(i.strip())
    final_holder = []
    for i in holder:
        if i:
            final_holder.append(i)
    command = final_holder[0]
    args = final_holder[1:]
    return command, args


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    if body:
        body = body.lower().strip()
        command, args = command_parser(body)
    else:
        command, args = '', []
    # Start our TwiML response
    resp = twiml.Response()
    answers = ['wifi', 'random']
    # Determine the right reply for this message
    if command not in answers:
        message = 'Here are a list of available commands:\n'
        answers.sort()
        for i in answers:
            message += i + '\n'
    else:
        if command == 'wifi':
            message = '536e7e6b93'
        elif command == 'random':
            message = randGen.rand_main(*args)
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)