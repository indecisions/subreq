#jaden
import Tkinter as tk
from Tkinter import *
from bs4 import BeautifulSoup
import requests
import subprocess
import time

def Main():

	subprocess.call('clear')
	input1 = raw_input("Web Address: ")
	
	window = tk.Tk()
	window.configure(background="black")
	window.title("nigger")
	window.geometry("620x520")

	title = tk.Label(bg="black", fg="white", text="skrt skrt")
	title.place(x=210, y=60)

	Links = "--#Links#--"
	Paragrahps = "--#Paragrahps#--"
	Comments = "--#Comments#--"
	hypertext1 = "--#Text[<h1>#--"
	tables = "--#Tables#--"

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
			for link3 in soup.find_all("br"):
				for link4 in soup.find_all('table'):

					results = Links, "\n\n", link1, "\n\n", Paragrahps, "\n\n", link2, "\n\n", Comments, "\n\n", hypertext1, "\n\n", tables, "\n\n", link4
			text = tk.Text(height=25, width=70)
			text.place(x=30, y=50)
			text.insert(tk.END, results,)
		scroll = tk.Scrollbar()

		window.mainloop()

Main()
