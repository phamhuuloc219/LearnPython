from guizero import App, Text, PushButton, TextBox, Combo, Slider, Picture

def change_color():
    text_test.value = txt_top.value
    # textt_test.value = txt_bottom.value
    text_test.text_color = color.value
    # textt_test.text_color = color.value
    text_test.text_size = slide.value
    # textt_test.text_size = slide.value
    text_test.font = font.value
    # textt_test.font = font.value
    pic_test.image= "D:\Learning\GitHub\LearnPython\Python\images\images.png"

app = App(title="Meme", height=800, width=700)

txt_title = Text(app,text="Hello",font="Arial",color="red",size=30)

txt_top = TextBox(app,text="Nhap van ban", height=30, width=100, command=change_color)
# txt_bottom = TextBox(app,text="Nhap van ban",height=30, width=100, command=change_color)

color = Combo(app,options=["black","red","blue","yellow","green"], selected="black", width=30, command=change_color)
font = Combo(app,options=["Times New Roman","Arial"],selected="Times New Roman", width=30, command=change_color)

slide = Slider(app,start=10,end=100,command=change_color)

text_test= Text(app,text="")
#textt_test= Text(app,text="")
pic_test = Picture(app, image="D:\Learning\GitHub\LearnPython\Python\images\Image_of_none.svg.png", height=500, width=600)

app.display()