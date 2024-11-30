from guizero import Picture, Text, App, PushButton
### wanted
# app = App(title="Wanted")


# app.bg = "#9FE2BF"
# message = Text(app,text="Itachi")
# message.font = "Time New Roman"
# message.text_size = 30
# message.text_color = "yellow"

# img = Picture(app, image=r"D:\Learning\GitHub\LearnPython\Python\images\images.png",height=500,width=400)

# message = Text(app,text="5.000.000 Rio")
# message.font = "Time New Roman"
# message.text_size = 30
# message.text_color = "yellow"

# hello
app = App(layout="auto")

def wanted():
    app.bg = "#9FE2BF"
    message = Text(app, text="Itachi")
    message.font = "Time New Roman"
    message.text_size = 50
    message.text_color = "yellow"

    img = Picture(app, image=r"D:\Learning\GitHub\LearnPython\Python\images\images.png", height=500, width=600)

    message = Text(app,text="5.000.000 Rio")
    message.font = "Time New Roman"
    message.text_size = 30
    message.text_color = "yellow"
    
def say_hello():
    message.value = "hello world"
    
def hide():
    message.hide()
    
def show():
    message.show()

def read_file():
    file_name.value = app.select_file()
    
message = Text(app)
file_name = Text(app)
# button_hello = PushButton(app, text="Press here", command=say_hello, height=1, width=10)
# button_hide = PushButton(app, text="Press hide", command=hide, height=1, width=10)
# button_show = PushButton(app, text="Press show", command=show, height=1, width=10)
button_wanted = PushButton(app, text="Wanted", command=wanted, height=1, width=10)
# PushButton(app, command=read_file,text="Get file")

app.display()

# from guizero import App, Text, PushButton, Box, Window, ListBox
# app = App(title="piCD", height=250)
# SelList = ListBox(app, grid=[0,1], align="center", scrollbar=True)
# for x in range(20):
#     SelList.append(str(x))
# #SelList.resize(450, 200)         # Works
# #SelList.resize(100, 200)        # Scroll bar disappears
# app.display()