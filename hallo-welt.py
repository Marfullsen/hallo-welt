#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hallo-welt.py, by Fr.Marfull (Oktober, 2019).
# version 1.0, tested on linux.

import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()

# show a message box
messagebox.showinfo("German Hello World","Hallo Welt!")
