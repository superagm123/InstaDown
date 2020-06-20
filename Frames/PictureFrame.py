import tkinter as tk 
from tkinter import ttk 
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from Instagram import Instagram

class PictureDownloader(ttk.Frame):
	def __init__(self, container, **kwargs):
		super().__init__(container)
		self['style'] = 'CustomFrame.TFrame'
		self.url_value = tk.StringVar()

		url_container = ttk.Frame(self, style='CustomFrame.TFrame')
		url_container.grid(column=0, row=0, sticky='EW')
		url_container.columnconfigure(1, weight=1)

		self.url_label = ttk.Label(url_container, text='url: ', style='CustomLabel.TLabel')
		self.url_entry = ttk.Entry(
			url_container, 
			textvariable=self.url_value,
			font=('TkDefaultFont', 15),
			foreground='green'
		)
		self.url_label.grid(column=0, row=0, sticky='W')
		self.url_entry.grid(column=1, row=0,columnspan=2, sticky='EW')

		download_container = ttk.Frame(self)
		download_container.grid(column=0, row=1, sticky='EW')
		download_container.columnconfigure(0, weight=1)

		self.download_button = ttk.Button(download_container, text='Download',command=self.download_picture)
		self.download_button['style'] = 'DownloadButton.TButton'
		self.download_button['cursor'] = 'hand2'
		self.download_button.grid(column=0, row=0, sticky='EW')

		for child in self.winfo_children():
			child.grid_configure(padx=15, pady=5)

	def download_picture(self):
		try: 
			instagram = Instagram()
			url = instagram.request_data(self.url_value.get())
			picture = instagram.get_picture(url)
			picture_content = instagram.get_picture_content(picture)
			files = [('JPEG', '*.jpg')]
			file = asksaveasfile(filetypes=files, mode='ab', defaultextension='.jpg')
			file.write(picture_content)
		except: 
			messagebox.showerror('Error trying to fetch data', 'Please enter a valid url')