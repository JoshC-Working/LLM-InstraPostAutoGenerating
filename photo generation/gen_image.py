from openai import OpenAI
import requests
client = OpenAI(api_key="")

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

response = requests.get(image_url)
with open("img.jpg", "wb") as file:
    file.write(response.content)