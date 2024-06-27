from PIL import Image, ImageDraw, ImageFont

def put_text(name1, text, font_size, padding, font_colour, background_colour, align = "centre" , font_path = None):
    img1 = Image.open("photo generation/photos/"+name1)
    width1, img_h = img1.size

    font_path = font_path or "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img1)

    # Text Handling 
    n = len(text)

    # Get text size

    left_padding = 40

    heights = [draw.textbbox((0, 0), text[i], font=font)[2:][1] + padding * 2 + 40 for i in range(n)]
    widths = [draw.textbbox((0, 0), text[i], font=font)[2:][0] + padding * 2 for i in range(n)]

    for i in range(n):
        x = left_padding
        y = (img_h - sum(heights)) / 2 + sum(heights[:i])

        rect_x0 = x - padding
        rect_y0 = y - padding
        rect_x1 = x + widths[i] + padding
        rect_y1 = y + heights[i] - 20 + padding

        draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill= background_colour)
        draw.text((x, y), text[i], font=font, fill=font_colour)

    """
    for i in range(n):
        text_width, text_height = draw.textbbox((0, 0), text[i], font=font)[2:] 
        print(text_width, text_height)  
        # Calculate position for the text
        if align == "centre":
            x = (width1 - text_width) / 2
            y = (img_h - (n)*(text_height+ 2* padding)) / 2 + (text_height + 2* padding)*i
        elif align == "left":
            x = left_padding
            y = (img_h - text_height) /2
        elif align == "right":
            x = width1 - left_padding-text_width
            y = (img_h - text_height) /2

        # Define rectangle bounds (adjust padding as needed)
        
        rect_x0 = x - padding
        rect_y0 = y - padding
        rect_x1 = x + text_width + padding
        rect_y1 = y + text_height + padding

        # Draw rectangle
        draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill= background_colour)

        # Draw text
        draw.text((x, y), text[i], font=font, fill=font_colour)
    """

    # Save the image
    img1.save('output.jpg')
    img1.show()

    pass



    


# # Load the image
# img = Image.open("photo generation/photos/photo_1.jpg")

# # Size of the image
# width, height = img.size

# # Define the text and font properties
# text = "Your Text Here"
# font_size = 100  # Adjust as needed to fit your image
# # Use the full path to the Arial Bold font
# font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
# font = ImageFont.truetype(font_path, font_size)

# # Create a draw object
# draw = ImageDraw.Draw(img)

# # Get text size
# text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
# x = (width - text_width) / 2
# y = (height - text_height) / 2

# # Calculate position for the text
# x = (width - text_width) / 2
# y = (height - text_height) / 2

# # Define rectangle bounds (adjust padding as needed)
# padding = 10
# rect_x0 = x - padding
# rect_y0 = y - padding
# rect_x1 = x + text_width + padding
# rect_y1 = y + text_height + padding

# # Draw rectangle
# draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill='orange')

# # Draw text
# draw.text((x, y), text, font=font, fill='white')

# # Save the image
# img.save('output.jpg')
# img.show()
