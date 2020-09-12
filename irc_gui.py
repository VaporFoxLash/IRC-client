#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import irc_functions
from irc_functions import print_response
from irc_functions import _channel_
from irc_functions import print_response
from irc_functions import MyClient
import irc


class Main_window:
    username = ""
    channel = ""
    commnd = ""

    def __init__(self, window):
        import tkinter as tk
        from tkinter import StringVar
        from tkinter import messagebox as mb
        self.window = window
        window.geometry("520x640")
        window.title(" Internet Relay Chat (IRC) client ")
        self.label = tk.Label(text="Welcome to Radebe-IRC")
        descrp = "Type your username and channeln. Channel must start with#"
        self.ds = tk.Label(text=descrp, bd=5)
        self.label.pack(pady=30, padx=30)
        self.ds.pack(pady=30, padx=30)

        _nickname = StringVar(window)
        _channel = StringVar()
        _cmd = StringVar()
        self.label.pack(pady=30, padx=30)

        command = ""
        _msg = StringVar()

        self.lbl_nickname = tk.Label(text='Nickname:')
        self.lbl_nickname.pack(pady=10, padx=10)
        self.ent_nickname = tk.Entry(window, textvariable=_nickname)
        self.ent_nickname.pack(pady=10, padx=10)

        self.lbl_nickname = tk.Label(text='Channel:')
        self.lbl_nickname.pack(pady=10, padx=10)

        username = _nickname.get()
        channel = _channel.get()
        _msg = StringVar()

        self.ent_channel = tk.Entry(window, textvariable=_channel)
        self.ent_channel.pack(pady=10, padx=30)

        self.joinButton = tk.Button(
            window, text="Join the channel", command=lambda: threading.Thread(
                target=irc.go(_nickname.get(), _channel.get())
            )
        )
        exitButton = tk.Button(
            window, text="Exit", command=self.exitApplication
        )
        inf = "To send message type "
        self.info = tk.Label(text='Channel:')
        self.joinButton.pack()
        exitButton.pack()

    def new_window(self):
        self.newwindow = ChatWindow()

    def errorMsg(self):
        mb.showerror("Error", "Enter your username and the channel")

    def exitApplication(self):
        import tkinter as tk
        MsgBox = tk.messagebox.askquestion("Exit Application",
                                           "Exit the application?",
                                           icon="warning")
        if MsgBox == 'yes':
            self.window.destroy()
            exit(0)

    def errorMsg(self):
        mb.showerror("Error", "Enter your username and the channel with #")

    def ExitApplication():
        MsgBox = tk.messagebox.askquestion("Exit Application",
                                           "Exit the application?",
                                           icon="warning")
        if MsgBox == 'yes':
            window.destroy()
            exit(0)


def main():
    import tkinter as tk
    root = tk.Tk()
    my_gui = Main_window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
