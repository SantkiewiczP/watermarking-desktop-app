from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

BACKGROUND_COLOR = "#F6F6F6"
BUTTON_COLOR = "#FFE2E2"
FONT_NAME = "arial.ttf"


def edit():
    count = 0
    filenames = filedialog.askopenfilenames(filetypes=[("image", ".jpeg"), ("image", ".jpg")])
    text = simpledialog.askstring("Text", "What text would you like to add to your picture?")
    font_size = simpledialog.askinteger("Size", "How big would you like your text to be?")
    new_name = simpledialog.askstring("File Name", "What would you like to save your edited photos as?")
    for file in filenames:
        count += 1
        font = ImageFont.truetype(FONT_NAME, font_size)
        image = Image.open(file)
        draw = ImageDraw.Draw(im=image)
        draw.text((15, 15), text=text, fill=(237, 230, 211), font=font)
        image.save(f"{new_name}{count}.jpg")


window = Tk()
window.title("Photo Watermarking App")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

upload_button = Button(text="Select images", bg=BUTTON_COLOR, fg="#8785A2", height=15, width=50, command=edit)
upload_button.pack()


upload_button.pack()

window.mainloop()
