from decouple import config
import openai

def get_message(message):
    openai.api_key = config("OPENAI_API_KEY")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )

    return response['choices'][0]['text']