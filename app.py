from tkinter import *
from chat import chat_tflearn, bot_name


back_gray = "#a5a694"
back_color = "#17202A"
text_color = "#EAECEE"

#FONT = "Helvetica 12"
FONT = "Times 15"
FONT_BOLD = "Helvetica 13 bold"

class chatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()


    def _setup_main_window(self):
        self.window.title("ChatBot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width =500, height =558, bg = back_color)

        #head leble
        head_label = Label(self.window, bg=back_color, fg=text_color,
                           text="JetBot", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        #tiny divider
        line = Label(self.window, width=300, bg=back_gray)
        line.place(relwidth=1, rely=0.07, relheight= 0.012)

        #text
        self.text_widget = Text(self.window, width=5, height=2,
                                bg="#5C554D", fg="#F6F5F4", font=FONT, pady=4, padx=4)
        self.text_widget.pack(side=LEFT, fill=BOTH, expand=True)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        #scroll bar
        scrollbar = Scrollbar(self.text_widget, orient=VERTICAL)
        scrollbar.place(relheight=1, relx=0.991)
        scrollbar.configure(command=self.text_widget.yview())


        #bottom label
        bottom_label = Label(self.window, bg=back_gray, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        #Mes entry
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg="#ADD8E6", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, relx=0.008, rely=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter)

        #Send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg= back_gray,
                             command=lambda :self._on_enter(None))
        send_button.place(relx=0.77,  rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter(self, event):
        msg=self.msg_entry.get()
        self._insert_msg(msg, "You")


    def _insert_msg(self, msg, sender):

        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {chat_tflearn(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__== "__main__":
    app = chatApplication()
    app.run()