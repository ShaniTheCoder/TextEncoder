# Imports
from tkinter import Label, Frame, StringVar, Button, PhotoImage, Tk, Entry
from tkinter.messagebox import showerror
import SecretCodeGenerator as scg
from pyperclip import copy

# Classs definatoin for structuring tkinter window
class TextEncoder(Tk):
    def __init__(self):
        """initializing the window"""
        super().__init__()
        self.geometry("371x460")
        self.minsize(371, 482)
        self.maxsize(371, 482)
        self.out = ""
        self.var = StringVar()
        icon = PhotoImage(file="resized_logo.png")
        self.geometry("371x460")
        self.iconphoto(True, icon)
        self.configure(bg="#444444")
        self.title("Secret text Encoder")

    def Choice(self, event):
        """This Function is responsible to let user decode and encode from user selection"""
        global out

        Scg = scg.SecretCodeLanguage()
        choice = event.widget.cget("text")
        if choice == "Encode":
            out = Scg.encode_string(self.inp.get())
        elif choice == "Decode":
            out = Scg.decode_string(self.inp.get())
        txt = self.truncate_text(out, 20)
        self.var.set(txt)
        self.text_copy()

    def text_copy(self):
        """Function to copy the text in text field to clip board"""
        global out
        copy(out)

    def truncate_text(self, text, length):
        """Shorten the message to fit the screen (no data is lost by copy user can view complete message)"""
        print(text)
        if len(text) > length:
            return text[:length-3] + "..."
        return text

    # The display window is divided into three scematics Header,Main and footer 
    def Header(self):
        """Function to render the header of the app"""
        # Frame
        self.frame_header = Frame(self, bg="#444444")
        self.frame_header.pack()
        self.frame_header.grid_columnconfigure(1, weight=1)
        # label & heading
        self.Heading = Label(self.frame_header, text="TextEncoder", bg="#444",
                             font="helvetica 20 bold", fg="white", borderwidth=2, relief="raised", padx=10, pady=4)
        self.Heading.grid(row=0, column=0, columnspan=2, pady=20)
        self.choice = Button(self.frame_header, text="Encode", bg="#333333", fg="cyan", borderwidth=3,
                             activebackground="#444444", activeforeground="white", padx=8,  relief="raised", font="helvetica 10 bold")
        self.choice1 = Button(self.frame_header, text="Decode", bg="#333333", fg="cyan", borderwidth=3,
                              activebackground="#444444", activeforeground="white", padx=8, relief="raised", font="helvetica 10 bold")

        self.choice.grid(row=1, column=0, sticky="e")
        self.choice1.grid(row=1, column=1, sticky="w")
        self.choice.bind("<Button-1>", self.Choice)
        self.choice1.bind("<Button-1>", self.Choice)

    def Main(self):
        """function to render main frame to window"""
        self.frame_main = Frame(self, bg="#444")
        self.frame_main.pack()
        self.inp = Entry(self.frame_main, font="verdana 10")
        self.inp.grid(row=2, column=1, pady=15, columnspan=2)
        Label(self.frame_main, text="Enter text: ", font="helvetica 15",
              fg="cyan", bg="#444").grid(row=2, column=0)

        result = Label(self.frame_main, textvariable=self.var,
                       font="verdana 15", bg="#444444", fg="cyan", wraplength=300,   padx=7, pady=5, justify="left")
        result.grid(row=4, column=0, pady=4, columnspan=2)

        Label(self.frame_main, text="Resulting Output: ", font="helvetica 15",
              fg="cyan", bg="#444").grid(row=3, column=0, columnspan=3)

        Button(self.frame_main, text="Copy", bg="#333", fg="cyan", font="helvetica 10     bold", activeforeground="white",
               activebackground="#444444", borderwidth=3, relief='raised', padx=8,   pady=4, command=self.text_copy).grid(columnspan=4, pady=8)

    def Footer(self):
        """function to render the footer of the app to the screen """
        self.frame_footer = Frame(self, bg="#444")
        self.frame_footer.pack(side="bottom")
        Button(self.frame_footer, text="Close", command=lambda: self.destroy(), bg="#333333", fg="cyan", borderwidth=3,
               activebackground="#444444", activeforeground="white", padx=8, pady=4, relief="raised", font="helvetica 10 bold").pack(side="bottom", pady=15)


if __name__ == "__main__":
    window = TextEncoder() 
    window.Header()
    window.Main()
    window.Footer()
    window.mainloop()
