import json
import traceback
import random


reprompt_texts = ["What else can I do for you?", "Is that all?", "Is that everything?",
                    "Anything else?", "Is there another license plate I can translate for you?",
                    "What other license plate can I help with?"]

phonetic_alphabet = {"alpha": "A", "adam": "A", "boy": "B", "bravo": "B", "charlie": "C",
    "delta": "D", "david": "D", "echo": "E", "edward": "E", "foxtrot": "F", "frank": "F",
    "golf": "G", "george": "G", "hotel": "H", "henry": "H", "india": "I", "ida": "I",
    "juliette": "J", "john": "J", "kilo": "K", "king": "K", "lima": "L", "lincoln": "L",
    "mike": "M", "mary": "M", "november": "N", "nora": "N", "oscar": "O", "ocean": "O",
    "papa": "P", "paul": "P", "quebec": "Q", "queen": "Q", "romeo": "R", "robert": "R",
    "sierra": "S", "sam": "S", "tango": "T", "tom": "T", "uniform": "U", "union": "U",
    "victor": "V", "whiskey": "W", "william": "W", "x-ray": "X","yankee": "Y", 
    "young": "Y", "zulu": "Z", "zebra": "Z"
}


#event: The event object, describing the type and attributes of the event
#context: The context for which the event occurred
#return: speech and card info to Alexa Skill
def lambda_handler(event, context):
    try:
        if event['request']['type'] == "LaunchRequest":
            return welcome_response()
        elif event['request']['type'] == "IntentRequest":
            return handle_intent(event['request'])
        elif event['request']['type'] == "SessionEndRequest":
            return handle_session_end(event['request'], event['session'])
    except:
        return error_response(True)

#end_request: request identification value
#session: the session associated with the end request
def handle_session_end(end_request, session):
    card_title = "Session Ended"
    speech_output = "License plate search program closing."
    return build_response({}, build_speech_response(card_title, speech_output,
        speech_output, True))

def welcome_response():
    card_title = "Welcome"
    speech_output = ("Hello. I am here to assist you with translating strings of " +
    "NATO phonetic words into license plate formats. What would you like to start " +
    "with?")
    reprompt_output = "What would you like for me to translate?"
    return build_response({}, build_speech_response(card_title, speech_output,
        reprompt_output, False))

#intent_request: data specific to the invokedintent
#return: call to the intent-specific function
def handle_intent(intent_request):
    try:
        intent_name = intent_request['intent']['name']
        intent_slots = intent_request['intent']['slots']
        if intent_name == "decodePhonetics":
            return decode_phonetics(intent_slots)
        else:
            raise ValueError("Invalid intent.")
    except:
        return error_response()


def decode_phonetics(intent_slots):
    try:
        state = intent_slots['state']['value']
        phonetic_words = (intent_slots['license_plate']['value']).split()
        license_plate = ""
        for word in phonetic_words:
            digit = phonetic_alphabet.get(word.lower(), None)
            if not digit: #outer try/except statement will catch error if word cant be evaluated
                number = eval(word)
                number_string = ""
                if type(number) == int:
                    while number / 10 > 0:
                        number_string = str(number % 10) + " " + number_string
                        number //= 10
                    license_plate += number_string
            else:
                license_plate += str(digit) + " "
        output_speech = str(state) + " license plate " + license_plate
        return build_answer(output_speech)
    except:
        return error_response(phonetic_string)


def error_response(phonetic_string = None, should_end_session = False):
    traceback.print_exc()
    if type(phonetic_string) == str:
        output_speech = "There was in a error in processing " + str(phonetic_string)
    else:
        output_speech = "Sorry, but I was unable to process your intended request"
    return build_response({}, build_speech_response("Error in processing your request", 
        output_speech, output_speech, should_end_session))


def build_answer(speech_output):
    index = random.randint(0, len(reprompt_texts) - 1)
    return build_response({}, build_speech_response("License Plate: ", speech_output,
        reprompt_texts[index], False))


def build_speech_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {"type": "PlainText", "text": output},
        "card": {"type": "Standard", "title": title, "context": output, "text": output},
        "reprompt": {"outputSpeech": {"type": "PlainText", "text": reprompt_text}},
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speech_reponse):
    return {"version": "1.0", "sessionAttributes": session_attributes,
        "response": speech_reponse
    }
