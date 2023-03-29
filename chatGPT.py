import openai

# It is recommended to set it as an environment variable and not as a string in code.
openai.api_key = # API key goes here.

# Using ASCI escape codes to make text look pretty.
print("\033[35;1;4mWelcome to the GPT-3.5 Turbo chatbot! Enter 'exit' to end the conversation.\x1b[0m")

# Need to set the messages variable like this. See https://platform.openai.com/docs/guides/chat/introduction for more info.
# It is best practice to include a system message in the start of the conversation as to initialize the bot.
# See https://platform.openai.com/docs/guides/chat/instructing-chat-models for more info.
messages = [
    {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. You are a helpful assistant."}
]

while True:
    userInput = input("\033[34;1mYou:\x1b[0m ")
    if userInput.lower() == "exit":
        print("\033[35;1mGoodbye!\x1b[0m")
        break
    else:
        messages.append(
            {"role": "user", "content": userInput},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages, 
            temperature = 0.5
        )
    
    # Parsing the response for just the reply. See https://platform.openai.com/docs/guides/chat/response-format for more info.
    response = chat.choices[0].message.content 
    print("\033[32;1mChatGPT:\x1b[0m " + response)
    messages.append({"role": "assistant", "content": response})
