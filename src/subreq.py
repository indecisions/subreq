import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import requests
import time

def Main():

	input1 = input("Web Address: ")
	
	window = tk.Tk()
	window.configure(background="black")
	window.title("Subreq")
	window.geometry("620x520")

	title = tk.Label(bg="black", fg="white", text="skrt skrt")
	title.place(x=210, y=60)

	Links = "@Links"
	Paragrahps = "@Paragrahps"
	Comments = "@Comments"
	tables = "@Tables"
	images = "@Images"

	try:
		r = requests.get(input1)
	except Exception as e:
		print(e)
		time.sleep(3)

	finally:
			print('\nrunning...')

	soup = BeautifulSoup(r.content, "lxml")

	for link1 in soup.find_all("a"):
		for link2 in soup.find_all("p"):
			for link3 in soup.find_all("img"):
				for link4 in soup.find_all('table'):

					results = Links, "\n\n", link1, "\n\n\n", Paragrahps, "\n\n\n", link2, "\n\n\n", images, "\n\n\n", link3, "\n\n\n", tables, "\n\n\n", link4, "\n\n\n",  
			text = tk.Text(height=25, width=70)
			text.place(x=30, y=50)
			text.insert(tk.END, results,)
		scroll = tk.Scrollbar()

		window.mainloop()

Main()

#made by @ja8den

