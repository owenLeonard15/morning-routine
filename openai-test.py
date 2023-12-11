from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are my supportive and positive personal assistant"},
    {"role": "user", "content": "My alarm clock just went off and I'm fighting the urge to go back to sleep. \
     Ask me some questions about machine learning to help me wake up and get my day started"},
  ]
)

print(completion.choices[0].message)

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=completion.choices[0].message.content,
)

response.stream_to_file("output.mp3")