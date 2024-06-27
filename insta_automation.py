# Reference
# https://medium.com/@sudhanshunamdev45/automating-instagram-posts-with-python-a-quick-guide-7d6031e0ce9d
# https://medium.com/@rajdattkokate/automate-instagram-posts-with-python-a-step-by-step-guide-4b055f356b31










import os
from PIL import Image
from instabot import Bot

def upload_image(username, password, image_path, caption):
    bot = Bot()
    bot.login(username="chak7777jjj", password="Tenir2004")

    # Load and resize the image
    img = Image.open(image_path)
    img = img.resize((1080, 1080))
    temp_image_path = "temp_image.jpg"
    img.save(temp_image_path)

    # Upload the image with the specified caption
    bot.upload_photo(temp_image_path, caption=caption)

    # Clean up temporary files
    os.remove(temp_image_path)

    bot.logout()

# # Input your Instagram credentials
# username = 1
# password = 2

# # Input the path to the image you want to upload
# image_path = "photos/photo_1.jpg"

# # Input the caption for your post
# caption = "jloo"

# upload_image(username, password, image_path, caption)


bot = Bot()
bot.login(username="happy_mochibellbell_lottie", password="josh2004")
bot.logout()
