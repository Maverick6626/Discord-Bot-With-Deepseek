from llm_chat import reply_llm, clear_memory
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
    elif command == 'clear':
        clear_memory(username)
        return username + ' idk you anymore'
    else:
        return 'I can\'t seem to understand try again'
