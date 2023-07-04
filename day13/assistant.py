import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import wikipedia
import webbrowser
import datetime

##########################################################

# Listen the mic and return text
def audio2text_transform():
    r = sr.Recognizer()
    # configure the mic
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("Listening...")
        # save audio
        audio = r.listen(source)
        try:
            # search the query in google
            text = r.recognize_google(audio,language="es-ar")
            # recognition test
            print(f'You say: {text}')
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "Sorry, i'don't understand"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Sorry, i can't find anything"
        except:
            return "Ups something went wrong"

#---------------------------------------------------------
def talk(msg,voice_dic,name):
    # power on the engine
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_dic[name]['id'])
    # Say msg
    engine.say(msg)
    # Run the engine
    engine.runAndWait()
#---------------------------------------------------------
def voice_query():
    engine = pyttsx3.init()
    voices = {}
    for voice in engine.getProperty('voices'):
        name = voice.id.split('_')[-2]
        lan  = voice.id.split('_')[-3]
        dic  = {'id':voice.id,'language':lan} 
        voices[name] = dic
    return voices

#---------------------------------------------------------
def query_day():
    day = datetime.datetime.today().weekday()
    calendar = {0:'lunes',1:'martes',2:'miercoles',3:'jueves',4:'viernes',5:'sabado',6:'domingo'}
    return f'hoy es {calendar[day]}'

#---------------------------------------------------------
def query_hour():
    hour = datetime.datetime.now()
    return f'la hora es {hour.hour} horas con {hour.minute} minutos y {hour.second} segundos'

#---------------------------------------------------------
def hello(name):
    hour = datetime.datetime.now().hour
    moment = ''
    if hour < 6 or hour > 20:
        moment = 'buenas noches'
    elif 6 <= hour < 13:
        moment = 'buenos dias'
    else:
        moment = 'buenas tardes'
    
    return f"{moment}, soy {name}, tu asistente personal"

#---------------------------------------------------------
def query_thinks(voiceDic,name):
    init = True
    while init:
        text = audio2text_transform().lower()

        if "abrir youtube" in text:
            talk("abriendo youtube",voiceDic,name)
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador" in text:
            talk("abriendo navegador",voiceDic,name)
            webbrowser.open("https://www.google.com")
            continue
        elif "qué dia es" in text:
            talk(query_day(),voiceDic,name)
            continue
        elif "qué hora es" in text:
            talk(query_hour(),voiceDic,name)
            continue
        elif "busca en wikipedia" in text:
            text = text.replace("busca en wikipedia","")
            wikipedia.set_lang("es")
            talk("buscando en wikipedia",voiceDic,name)
            result = wikipedia.summary(text, sentences=1)
            talk(result,voiceDic,name)
            continue
        elif "busca en internet" in text:
            text = text.replace("busca en internet","")
            pywhatkit.search(text)
            continue
        elif "reproducir" in text:
            text = text.replace("reproducir","")
            pywhatkit.playonyt(text)
            continue
        elif "chiste" in text:
            talk(pyjokes.get_joke(),voiceDic,name)
            continue
        elif "acciones" in text:
            stokes = text.split('de')[-1].strip()
            portfolio = {'apple':'APPL',
                         'google':'GOOG',
                         'amazon':'AMZN'}
            try:
                stoke_searching = portfolio[stokes]
                stoke_searching = yf.Ticker(stoke_searching)
                price = stoke_searching.info['regularMarketPrice']
                talk(f"el precio de {stokes} es {price}",voiceDic,name)
            except:
                talk("ups algo salio mal, no la he encontrado",voiceDic,name)
            continue
        elif "adios" in text:
            talk("Gracias por usar mis servicios",voiceDic,name)
            init = False

##########################################################


voiceDic = voice_query()
print('These are the voices you can choose:')
for voice in voiceDic:
    print(f'{voice}, who speaks in {voiceDic[voice]["language"]}')

name = input('What voice would you like to use?\n>>> ')

talk(hello(name),voiceDic,name)
query_thinks(voiceDic,name)
