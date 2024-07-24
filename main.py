from flask import Flask,jsonify,request
from bot import ConversationBot
import os


app = Flask(__name__)
bot = ConversationBot(api_key=os.environ['GROQ_API_KEY'])


@app.route('/')
def initialRoute():
    return """<h3>Bot is up</h3>"""


@app.route('/getReply', methods = ['POST'])
def getReply():
    data = request.get_json()
    lastMessages = data['last_messages']
    userMessage = data['user_message']

    return jsonify({'response':bot.converse(userMessage,lastMessages)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)