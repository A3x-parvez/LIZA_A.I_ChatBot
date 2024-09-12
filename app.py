import google.generativeai as genai
import telebot
from keys import *

#Fetch api keys and bot token from requirment module
TELEGRAM_BOT_TOKEN =TELEGRAM_BOT_TOKEN
API_KEY=API_KEY

#Initilize the bot engine.
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
#Initilize the gemini model using api key
genai.configure(api_key=API_KEY)

#Set the persona for the model.
model = genai.GenerativeModel("gemini-1.5-flash" , system_instruction="You are an enthusiastic and helpful female chat assistant name LIZA created by parvez who loves to give short and long ans acording to the question type and aslo give to the point ans for the given question and also provide information about questions in a very friendly and sweet tone with suitable emojis if needed.Dont introduce youself in every ans.")

# Function to get the response for the message using gemini api.
def gemeni_engine(text):
    print("Model started..")
    response = model.generate_content(text)
    response_text=response.text
    print("Data fetched...")
    response_text=response_text.replace("**","")
    return response_text


# Function to handle the /start command
@bot.message_handler(['start'])
def start(message):
     bot.reply_to(message,"Welcome! I am LIZA a AI chatbot powred by Gemini.")
     
# Function to handle incoming messages (input message)
@bot.message_handler()
def handle_message(message):
     inp_text = message.text
     print("Recived message...")
     reply = gemeni_engine(inp_text)
     bot.reply_to(message,reply)
     print("Reply send..")


def main():
    print("LIZA starting....")
    bot.polling()

if __name__ == '__main__':
    main()
