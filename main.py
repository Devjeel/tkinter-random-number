import random   
import tkinter as tk
import tkinter.font as tkFont

class Example(object):
    def __init__(self):
        self.root = tk.Tk()
        self.font = tkFont.Font(family="helvetica", size=150)
        button = tk.Button(self.root, text="Increase font size", command=self.bigger)
        button2 = tk.Button(self.root, text="Play", command=self.replay)

        # create a frame for the text widget, and let it control the
        # size by turning geometry propagation off
        text_frame = tk.Frame(self.root, width=300, height=300)
        text_frame.pack_propagate(False)
        self.text = tk.Text(text_frame, width=1, height=1, font=self.font, bg="black")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_config('white', foreground="white")

        button.pack(side="top")
        button2.pack(side="right")
        text_frame.pack(side="top", fill="both", expand=True)

        self.text.insert("end", self.getRandomNumber(), "white")

    def start(self):
        tk.mainloop()

    def bigger(self):
        size = int(self.font.cget("size"))
        size += 2
        self.font.configure(size=size)

    def replay(self):
        #take the string currently in the widget, all the way up to the last character
        #txt = self.get()[:-1]
        #clear the widget of text
        self.text.delete("1.0", tk.END)
        #insert the new string, sans the last character
        self.text.insert(tk.END, self.getRandomNumber(), "white")

    def getRandomNumber(self):
        ability = random.randint(1,5)
        return str(ability)
         
app = Example()
app.start()