import re

def match_intent(msg, patterns):
    msg = msg.lower()
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern, msg):
            matched_intent = intent

    return matched_intent

intents = {
    'greet': ['hi','hello','hey','bot'],
    'fine': ['how are you (.*)','how do you do (.*)','how are you','how do you do'],
    'self_intro':['(.*) about you','who are you?','what can you do','what can you do (.*)'],
    
    'go_left': ['left', 'turn left','move left','go left'],
    'go_right': ['right', 'turn right','move right','go right'],
    'go_straight': ['straight', 'forward','turn straight','move straight','go straight'],
    'go_back': ['back', 'turn back','move back','go back'],

    'stop': ['quit', 'exit', ' stop', 'close', 'thank you (.*)', 'thank', 'bye', 'goodbye'],
}


responses = {
    'default': ['Sorry, it is beyond my ability.'],
    'greet': ['Hi! ,what can I do for you?', 'Good to see you, how can I help you?'],
    'fine': ['I am fine. Thank you so much for asking!'],
    
    'self_intro':['Self introduction.'],
    'go_left': ['Moving Left'],
    'go_right': ['Moving Right'],
    'go_straight': ['Moving Straight'],
    'go_back': ['Moving Back'],

    'stop': ['goodbye'],
}


patterns = {}
for intent, values in intents.items():
    patterns[intent] = re.compile(r'|'.join(values))


# while True:
#     msg=input()
#     print(match_intent(msg, patterns))