import tkinter as tk 
import tkinter.font as font
from tkinter import ttk 
from Frames import PictureDownloader

BUTTON_COLOR = '#00994d'
BUTTON_ACTIVE_COLOR = '#008040'
BACKGROUND_COLOR = '#fff'
LIGHT_TEXT = '#fff'
DARK_TEXT = '#000'

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.geometry('400x200')
		self.title('InstaDown 0.1')
		self.resizable(False, False)
		self['background'] = BACKGROUND_COLOR
		self.style = ttk.Style(self)
		self.style.theme_use('clam')
		self.style.configure('CustomFrame.TFrame', background=BACKGROUND_COLOR)
		self.style.configure(
			'DownloadButton.TButton',
			 background=BUTTON_COLOR,
			 foreground=LIGHT_TEXT
		)
		self.style.map(
			'DownloadButton.TButton',
			background=[('active', BUTTON_ACTIVE_COLOR)]
		)
		self.style.configure(
			'CustomLabel.TLabel',
			 background=BACKGROUND_COLOR,
			 foreground=DARK_TEXT
	    )

		container = ttk.Frame(self)
		container.grid(padx=20, pady=10, sticky='EW')
		container.columnconfigure(0, weight=1)

		frame = PictureDownloader(container)
		frame.grid(column=0,row=0, sticky='NSEW')
		frame.columnconfigure(0, weight=1)


if __name__ == '__main__':
	app = App()
	app.columnconfigure(0, weight=1)
	app.rowconfigure(0, weight=1)
	font.nametofont('TkDefaultFont').configure(size=12)
	app.mainloop()