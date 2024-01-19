import openai
openai.api_key="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"
def get_response(input):
    response = openai.Completion.create(
    model="text_davinci-003",
    prompt=input
    )
    return response

if__name__="__main__"
print("Chatbot: Hii User!! May I help you?")
user_input= input("User: ")
response= get_response(user_input)
print(response)