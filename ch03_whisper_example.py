import openai

openai.api_key = "sk-proj-9J4Dw9QrzfO9Tale0FyNT3BlbkFJQjx1xZLzK9elXFO0HqlO"

audio_file = open('output.mp3', 'rb')
transcript = openai.Audio.transcribe('whisper-1', audio_file)
print(transcript['text'])