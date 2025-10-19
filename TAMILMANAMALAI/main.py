from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")
    print("User:", incoming_msg)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for TamilManamali, a Tamil matrimony website. Speak in polite Tamil and guide users through registration, plan details, or help."},
            {"role": "user", "content": incoming_msg}
        ]
    )
    reply_text = response.choices[0].message.content.strip()

    reply = MessagingResponse()
    reply.message(reply_text)
    return str(reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
