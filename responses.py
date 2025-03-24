from rude_chat import reply_llm
from comp_and_insult import insult, compliment
from random import randint

def get_response(user_input: str, username: str) -> str:
    lowered = user_input.lower()
    command = ''

    for _ in lowered:
        if _ == ' ':
            break
        command += _
    lowered = lowered[len(command)+1:]
    if command == 'chat':
        return reply_llm(username, lowered)
    elif command == 'compliment':
        return compliment()
    elif command == 'insult':
        return insult()
    else:
        return 'I can\'t seem to understand try again'
