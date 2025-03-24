from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

# Initialize the Ollama Model
llm = OllamaLLM(model='deepseek-r1')

# Initialize memory store (a dictionary to track user messages)
user_memory = {}

# Prompt
friend_prompt = PromptTemplate(
    input_variables=['username', 'history', 'question'],
    template="""
    You are a friendly chatbot named HomelessDino.
    Chat with the user like a friend.
    Your response should:
    - Be sweet.
    - Be at most 50 words.
    - Be concise, clear, and confident.

    Previous conversation history:
    {history}

    Question: {question}

    Response:
    """
)

friend_llm = friend_prompt | llm


def reply_llm(username: str, question: str) -> str:
    if username not in user_memory:
        user_memory[username] = []
    user_memory[username].append(f"User: {question}")

    history = "\n".join(user_memory[username][-10:])  # Keep only the last 10 messages
    answer = friend_llm.invoke({"username": username, "history": history, "question": question})
    user_memory[username].append(f"Bot: {answer}")
    c1, c2 = 0, 0
    for _ in answer:
        if _ == '>':
            c1 += 1
        c2 += 1
        if c1 == 2:
            break
    answer = answer[c2 + 1:]

    return answer


if __name__ == '__main__':
    username = "john_doe"

    # Test interaction
    print(reply_llm(username, "Hello, tell me a number from 1 to 100"))
    print(reply_llm(username, "Tell me the previous number and multiply 2 to it"))
    print(reply_llm(username, "Now subtract 5 from that number"))
