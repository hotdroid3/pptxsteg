from ttkthemes import themed_tk as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import filedialog
import os

def main():
	"""This is the main function.
	If this module is executed as a script, execution will commence in this function.
	"""
	window = tk.ThemedTk()
	window.title('PowerPoint Steganography Application')
	window.geometry('400x300')
	window.set_theme('arc')

	ch_pptx_lbl = ttk.Label(window, text='Choose cover PowerPoint file: ')
	#  font=('Lucida Console', 12), width = 30
	ch_pptx_lbl.grid(column=0, row=0, padx=30, pady=20)

	browse_pptx_btn = ttk.Button(window, text='Browse', command=_browse_pptx_clicked)
	# bg = ('#4e92df'), width = 10
	browse_pptx_btn.grid(column=1, row=0, padx=5, pady=20)






	window.mainloop()

def _browse_pptx_clicked():

	file = filedialog.askopenfilename(filetypes=(('PowerPoint 2007 files', '*.pptx'),), initialdir=os.getcwd())
	return file


if __name__ == '__main__':
	main()