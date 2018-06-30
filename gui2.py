from ttkthemes import themed_tk as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import filedialog
import os

class GraphicalUserInterface():
	"""Graphical User Interface for PowerPoint Steganography Application"""
	def __init__(self):
		super().__init__()
		self.pptx_file = ''
		self.embed_file = ''
		self.window = tk.ThemedTk()
		self.window.title('PowerPoint Steganography Application')
		self.window.geometry('1024x768')
		self.window.set_theme('arc')

		self.ch_pptx_lbl = ttk.Label(self.window, text='Choose Cover PowerPoint File: ') #  font=('Lucida Console', 12), width = 30
		self.ch_pptx_lbl.grid(column=0, row=0, padx=130, pady=20)

		self.browse_pptx_btn = ttk.Button(self.window, text='Browse', command=self.browse_pptx_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.browse_pptx_btn.grid(column=1, row=0, padx=5, pady=20)

		self.se_pptx_lbl = ttk.Label(self.window, text='Selected PowerPoint File: ') #  font=('Lucida Console', 12), width = 30
		self.se_pptx_lbl.grid(column=0, row=1, padx=30, pady=5)

		self.pptx_file_lbl = ttk.Label(self.window, text=self.pptx_file) #  font=('Lucida Console', 12), width = 30
		self.pptx_file_lbl.grid(column=1, row=1, padx=5, pady=5)

		self.embed_rad = ttk.Radiobutton(self.window, text='Embed', value=1, command=self.embed_rad_clicked)
		self.embed_rad.grid(column=0, row=2, padx=130, pady=30)

		self.extract_rad = ttk.Radiobutton(self.window, text='Extract', value=2, command=self.extract_rad_clicked)
		self.extract_rad.grid(column=1, row=2, padx=30, pady=30)

		self.embed_file_rad = ttk.Radiobutton(self.window, text='Embed From File', value=3, command=self.embed_file_rad_clicked)
		self.embed_file_rad.grid(column=0, row=3, padx=130, pady=15)
		self.embed_file_rad.grid_remove()

		self.sel_emb_file = ttk.Label(self.window, text='Select File to Embed: ') #  font=('Lucida Console', 12), width = 30
		self.sel_emb_file.grid(column=0, row=4, padx=130, pady=15)
		self.sel_emb_file.grid_remove()

		self.sel_emb_file_btn = ttk.Button(self.window, text='Browse', command=self.sel_emb_file_btn_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.sel_emb_file_btn.grid(column=1, row=4, padx=30, pady=15)
		self.sel_emb_file_btn.grid_remove()

		self.em_file_lbl = ttk.Label(self.window, text='Selected File To Embed: ') #  font=('Lucida Console', 12), width = 30
		self.em_file_lbl.grid(column=0, row=5, padx=130, pady=15)
		self.em_file_lbl.grid_remove()

		self.embed_file_lbl = ttk.Label(self.window, text=self.embed_file) #  font=('Lucida Console', 12), width = 30
		self.embed_file_lbl.grid(column=1, row=5, padx=30, pady=15)
		self.embed_file_lbl.grid_remove()

		self.enc_file_lbl = ttk.Label(self.window, text='Encrypt file: ') #  font=('Lucida Console', 12), width = 30
		self.enc_file_lbl.grid(column=0, row=6, padx=130, pady=15)
		self.enc_file_lbl.grid_remove()

		self.enc_file_y = ttk.Radiobutton(self.window, text='Yes', value=7)
		self.enc_file_y.grid(column=1, row=6, padx=0, pady=15)
		self.enc_file_y.grid_remove()

		self.enc_file_n = ttk.Radiobutton(self.window, text='No', value=8)
		self.enc_file_n.grid(column=2, row=6, padx=0, pady=15)
		self.enc_file_n.grid_remove()


		self.embed_msg_rad = ttk.Radiobutton(self.window, text='Embed a Secret Message', value=4, command=self.embed_msg_rad_clicked)
		self.embed_msg_rad.grid(column=1, row=3, padx=30, pady=15)
		self.embed_msg_rad.grid_remove()


		self.emb_enc_lbl = ttk.Label(self.window, text='Was Embedded File Encrypted?') #  font=('Lucida Console', 12), width = 30
		self.emb_enc_lbl.grid(column=0, row=3, padx=130, pady=15)
		self.emb_enc_lbl.grid_remove()

		self.emb_enc_y = ttk.Radiobutton(self.window, text='Yes', value=5)
		self.emb_enc_y.grid(column=1, row=3, padx=0, pady=15)
		self.emb_enc_y.grid_remove()

		self.emb_enc_n = ttk.Radiobutton(self.window, text='No', value=6)
		self.emb_enc_n.grid(column=2, row=3, padx=0, pady=15)
		self.emb_enc_n.grid_remove()




		self.window.mainloop()
		

	def browse_pptx_clicked(self):
		self.pptx_file = filedialog.askopenfilename(filetypes=(('PowerPoint 2007 files', '*.pptx'),), initialdir=os.getcwd())
		self.pptx_file_lbl.config(text=self.pptx_file)

	def embed_rad_clicked(self):
		self.embed_file_rad.grid()
		self.embed_msg_rad.grid()
		self.emb_enc_lbl.grid_remove()
		self.emb_enc_y.grid_remove()
		self.emb_enc_n.grid_remove()
		self.sel_emb_file.grid_remove()
		self.em_file_lbl.grid_remove()
		self.sel_emb_file_btn.grid_remove()
		self.embed_file_lbl.grid_remove()
		


	def extract_rad_clicked(self):
		self.emb_enc_lbl.grid()
		self.emb_enc_y.grid()
		self.emb_enc_n.grid()
		self.embed_file_rad.grid_remove()
		self.embed_msg_rad.grid_remove()
		self.sel_emb_file.grid_remove()
		self.em_file_lbl.grid_remove()
		self.sel_emb_file_btn.grid_remove()
		self.embed_file_lbl.grid_remove()
		self.enc_file_lbl.grid_remove()
		self.enc_file_y.grid_remove()
		self.enc_file_n.grid_remove()

	def embed_msg_rad_clicked(self):
		self.sel_emb_file.grid_remove()
		self.em_file_lbl.grid_remove()
		self.sel_emb_file_btn.grid_remove()
		self.embed_file_lbl.grid_remove()

	def sel_emb_file_btn_clicked(self):
		self.embed_file = filedialog.askopenfilename(filetypes=(('All files', '*.*'),), initialdir=os.getcwd())
		self.em_file_lbl.grid()
		self.embed_file_lbl.grid()
		self.embed_file_lbl.config(text=self.embed_file)
		self.enc_file_lbl.grid()
		self.enc_file_y.grid()
		self.enc_file_n.grid()

	def embed_file_rad_clicked(self):
		self.sel_emb_file.grid()
		self.sel_emb_file_btn.grid()


def main():
	"""This is the main function.
	If this module is executed as a script, execution will commence in this function.
	"""
	GraphicalUserInterface()

if __name__ == '__main__':
	main()