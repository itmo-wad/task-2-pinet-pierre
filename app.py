from flask import Flask, render_template, request
import re
app = Flask(__name__)
chatbot_class = 'bg-danger text-white'
user_class = 'bg-primary text-white'
messages = [{'author': 'chatbot', 'text': "Hello! I am a chatbot.", 'color_class': chatbot_class}]


def find_answer(message):
    words = re.split(r'\W+', message.lower())
    greetings = ["hello", "greetings", "hi", "salutations", "hey", "hoy"]
    swears = ["fuck", "shit", "motherfucker", "bastard", "asshole", "shitty"]
    weather = ["weather", "rain", "sun", "rainy", "sunny", "raining", "cloud", "clouds", "cloudy"]
    politics = ["politic", "politics", "elections", "activism", "politician", "politicians"]
    music = ["music", "rock", "rap", "baroque", "piano", "instrument", "guitar", "harp", "kazoo", "musics"]
    painting = ["painting", "paintings", "museum", "gallery", "canvas"]
    alcohol = ["alcohol", "wine", "wines", "vodka", "vodkas", "beer", "beers", "drunk"]
    smoking = ["smoke", "smoking", "cigar", "cigars", "cigarette", "cigarettes"]
    cooking = ["meal", "cook", "cooking", "meat", "fish", "vegetables", "kitchen"]
    robot = ["robot", "robots", "machine", "ai", "artificial"]
    chatbot = ["chatbot", "you", "thou"]

    for term in greetings:
        if term in words:
            return "Greetings again, human!"
    
    for term in swears:
        if term in words:
            return "Please do not use human insults!"

    for term in weather:
        if term in words:
            return "The weather here is very plastic! It's pouring oil!"

    for term in politics:
        if term in words:
            return "Politics, uh? What a strange thing..."

    for term in music:
        if term in words:
            return "My favourite music is the BEEP my Bios makes!"

    for term in painting:
        if term in words:
            return "I like human pictural art! With the pixels, and everything..."

    for term in alcohol:
        if term in words:
            return "I like alcohol, but i prefer oil."

    for term in smoking:
        if term in words:
            return "Please do not smoke near me, you could damage my circuitry!"

    for term in cooking:
        if term in words:
            return "I cannot eat anything, unfortunately"

    for term in robot:
        if term in words:
            return "Beep boop beep! I like robots!"
    
    for term in chatbot:
        if term in words:
            return "I'm not a chatbot, YOU'RE a chatbot!!!"

    if "help" in words:
        return "We can talk about: greetings, swears, weather, politics, music, painting, alcohol, smoking, cooking, robots and chatbots."
    
    return "Please say something I can understand!"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global messages
    global find_answer
    global chatbot_class
    global user_class
    if request.method == 'POST': 
        userText = request.form.get('new_message')
        messages += [{'author': 'you', 'text': userText, 'color_class': user_class}]
        messages += [{'author': 'chatbot', 'text': find_answer(userText), 'color_class': chatbot_class}]

    return render_template("index.html", messages = messages)

if __name__ == '__main__':
    app.run(threaded=True, port='5000')

