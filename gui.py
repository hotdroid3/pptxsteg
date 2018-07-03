from ttkthemes import themed_tk as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import filedialog
from tkinter import messagebox
from pptx.exc import PackageNotFoundError
from pptxsteg import EmbedExtract, InsufficientCapacityError
from codec import EncoderDecoder, FileNameTooLongError

import os

class MainGUI():
	"""Graphical User Interface for PowerPoint Steganography Application"""
	def __init__(self):
		super().__init__()

		if 'output' not in os.listdir(os.getcwd()):
			os.mkdir('output')

		self.pptx_file = ''
		self.embed_file = ''
		self.key_file = ''
		self.psc = ''
		self.window = tk.ThemedTk()
		self.window.title('PowerPoint Steganography Application')
		self.window.geometry('1366x768')
		self.window.set_theme('plastik')

		self.ch_pptx_lbl = ttk.Label(self.window, text='Choose Cover PowerPoint File: ') #  font=('Lucida Console', 12), width = 30
		self.ch_pptx_lbl.grid(column=0, row=0, padx=130, pady=20)

		self.browse_pptx_btn = ttk.Button(self.window, text='Browse', command=self.browse_pptx_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.browse_pptx_btn.grid(column=1, row=0, padx=5, pady=20)

		self.se_pptx_lbl = ttk.Label(self.window, text='Selected PowerPoint File: ') #  font=('Lucida Console', 12), width = 30
		self.se_pptx_lbl.grid(column=0, row=1, padx=130, pady=5)

		self.pptx_file_lbl = ttk.Label(self.window, text=self.pptx_file) #  font=('Lucida Console', 12), width = 30
		self.pptx_file_lbl.grid(column=1, row=1, padx=5, pady=5)

		self.psc_lbl = ttk.Label(self.window, text='PowerPoint Steganographic Capacity: ') #  font=('Lucida Console', 12), width = 30
		self.psc_lbl.grid(column=0, row=2, padx=130, pady=20)

		self.psc_result = ttk.Label(self.window, text=self.psc) #  font=('Lucida Console', 12), width = 30
		self.psc_result.grid(column=1, row=2, padx=5, pady=20)

		self.embed_rad = ttk.Radiobutton(self.window, text='Embed', value=1, command=self.embed_rad_clicked)
		self.embed_rad.grid(column=0, row=3, padx=130, pady=30)
		self.embed_rad.grid_remove()

		self.extract_rad = ttk.Radiobutton(self.window, text='Extract', value=2, command=self.extract_rad_clicked)
		self.extract_rad.grid(column=1, row=3, padx=30, pady=30)
		self.extract_rad.grid_remove()

		
		self.window.mainloop()
		

	def browse_pptx_clicked(self):
		self.pptx_file = filedialog.askopenfilename(filetypes=(('PowerPoint 2007 files', '*.pptx'),), initialdir=os.getcwd())

		try:
			pptx_obj = EmbedExtract(self.pptx_file)
		except PackageNotFoundError as e:
			messagebox.showinfo('Error!','Selected PowerPoint file does not exist!')
			self.pptx_file_lbl.config(text='')
			self.psc_result.config(text='')
		else:
			self.pptx_file_lbl.config(text=self.pptx_file)

			pptx_cap = str(pptx_obj.calculate_capacity()) + ' bytes'
			self.psc_result.config(text=pptx_cap)

			self.embed_rad.grid()
			self.extract_rad.grid()




			

	def embed_rad_clicked(self):
		if self.pptx_file != '':
			EmbedGUI(self)
		else:
			messagebox.showinfo('Error!','Selected PowerPoint file does not exist!')
		
	def extract_rad_clicked(self):
		if self.pptx_file != '':
			ExtractGUI(self)
		else:
			messagebox.showinfo('Error!','Selected PowerPoint file does not exist!')


class EmbedGUI():
	"""GUI for embedding steganograms"""
	def __init__(self, root):
		super().__init__()
		self.root = root
		self.embed_file = ''
		self.encrypt = None
		self.window = tk.ThemedTk()
		self.window.title('PowerPoint Steganography Application')
		self.window.geometry('1366x768')
		self.window.set_theme('plastik')
		self.window.lift()


		self.sel_emb_file = ttk.Label(self.window, text='Select File to Embed: ') #  font=('Lucida Console', 12), width = 30
		self.sel_emb_file.grid(column=0, row=0, padx=130, pady=20)

		self.sel_emb_file_btn = ttk.Button(self.window, text='Browse', command=self.sel_emb_file_btn_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.sel_emb_file_btn.grid(column=1, row=0, padx=30, pady=20)

		self.em_file_lbl = ttk.Label(self.window, text='Selected File To Embed: ') #  font=('Lucida Console', 12), width = 30
		self.em_file_lbl.grid(column=0, row=1, padx=130, pady=15)
		self.em_file_lbl.grid_remove()

		self.embed_file_lbl = ttk.Label(self.window, text=self.embed_file) #  font=('Lucida Console', 12), width = 30
		self.embed_file_lbl.grid(column=1, row=1, padx=30, pady=15)
		self.embed_file_lbl.grid_remove()

		self.enc_file_lbl = ttk.Label(self.window, text='Encrypt file: ') #  font=('Lucida Console', 12), width = 30
		self.enc_file_lbl.grid(column=0, row=2, padx=0, pady=15)
		self.enc_file_lbl.grid_remove()

		self.enc_file_y = ttk.Radiobutton(self.window, text='Yes', value=1, command=self.enc_file_y)
		self.enc_file_y.grid(column=1, row=2, padx=0, pady=15)
		self.enc_file_y.grid_remove()

		self.enc_file_n = ttk.Radiobutton(self.window, text='No', value=2, command=self.enc_file_n)
		self.enc_file_n.grid(column=2, row=2, padx=0, pady=15)
		self.enc_file_n.grid_remove()

		self.embed_btn = ttk.Button(self.window, text='Embed', command=self.embed_btn_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.embed_btn.grid(column=2, row=3, padx=0, pady=15)
		self.embed_btn.grid_remove()

		self.window.mainloop()
		


	def sel_emb_file_btn_clicked(self):
		self.embed_file = filedialog.askopenfilename(filetypes=(('All files', '*.*'),), initialdir=os.getcwd())
		self.root.embed_file = self.embed_file

		self.em_file_lbl.grid()
		self.embed_file_lbl.grid()
		self.embed_file_lbl.config(text=self.embed_file)

		self.enc_file_lbl.grid()
		self.enc_file_y.grid()
		self.enc_file_n.grid()

		self.embed_btn.grid()
		self.window.lift()

	def enc_file_y(self):
		self.encrypt = True

	def enc_file_n(self):
		self.encrypt = False

	def embed_btn_clicked(self):
		if self.encrypt is None:
			messagebox.showinfo('Error!','Please select to encrypt or not to encrypt the file to be embedded!')
		elif self.encrypt:
			try:
				hex_strings = EncoderDecoder.encode_from_file(self.embed_file, encryption=self.encrypt)
			except FileNameTooLongError as err:
				messagebox.showinfo('Error!', str(err))
			except FileNotFoundError as err:
				messagebox.showinfo('Error!', str(err))
			else:
				hex_strings, key = hex_strings
				with open('output\\key.bin', 'wb') as keyfile:
					keyfile.write(key)
				messagebox.showinfo('Notification:','Your encryption key has been saved at: {}\\key.bin'.format(os.getcwd()))

				try:
					embed_pptx = EmbedExtract(self.root.pptx_file)
				except PackageNotFoundError as e:
					messagebox.showinfo('Error!','Selected PowerPoint file does not exist!')
					self.window.destroy()
				else:
					try:
						embed_pptx.embed_hex(hex_strings)
					except InsufficientCapacityError as err:
						messagebox.showinfo('Error!',str(err))
						self.window.destroy()
					else:
						embed_pptx.save_pptx()
						messagebox.showinfo('Success!', 'Successfully embedded file into selected cover PowerPoint file!')
						self.window.destroy()
				
				
		else:
			try:
				hex_strings = EncoderDecoder.encode_from_file(self.embed_file)
			except FileNameTooLongError as err:
				messagebox.showinfo('Error!', str(err))
			except FileNotFoundError as err:
				messagebox.showinfo('Error!', str(err))
			else:
				try:
					embed_pptx = EmbedExtract(self.root.pptx_file)
				except PackageNotFoundError as e:
					messagebox.showinfo('Error!','Selected PowerPoint file does not exist!')
					self.window.destroy()
				else:
					try:
						embed_pptx.embed_hex(hex_strings)
					except InsufficientCapacityError as err:
						messagebox.showinfo('Error!',str(err))
						self.window.destroy()
					else:
						embed_pptx.save_pptx()
						messagebox.showinfo('Success!', 'Successfully embedded file into selected cover PowerPoint file!')
						self.window.destroy()



class ExtractGUI():
	"""GUI for embedding steganograms"""
	def __init__(self, root):
		super().__init__()
		self.root = root
		self.key_file = ''
		self.encrypt = None
		self.window = tk.ThemedTk()
		self.window.title('PowerPoint Steganography Application')
		self.window.geometry('1366x768')
		self.window.set_theme('plastik')
		self.window.lift()


		self.dec_file_lbl = ttk.Label(self.window, text='Is embedded file encrypted?') #  font=('Lucida Console', 12), width = 30
		self.dec_file_lbl.grid(column=0, row=0, padx=130, pady=20)

		self.dec_file_y = ttk.Radiobutton(self.window, text='Yes', value=1, command=self.dec_file_y)
		self.dec_file_y.grid(column=1, row=0, padx=0, pady=20)

		self.dec_file_n = ttk.Radiobutton(self.window, text='No', value=2, command=self.dec_file_n)
		self.dec_file_n.grid(column=2, row=0, padx=0, pady=20)

		self.sel_key_file = ttk.Label(self.window, text='Select Encryption Key File: ') #  font=('Lucida Console', 12), width = 30
		self.sel_key_file.grid(column=0, row=1, padx=130, pady=15)
		self.sel_key_file.grid_remove()

		self.sel_key_file_btn = ttk.Button(self.window, text='Browse', command=self.sel_key_file_btn_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.sel_key_file_btn.grid(column=1, row=1, padx=30, pady=15)
		self.sel_key_file_btn.grid_remove()

		self.key_file_lbl = ttk.Label(self.window, text='Selected Key File: ') #  font=('Lucida Console', 12), width = 30
		self.key_file_lbl.grid(column=0, row=2, padx=130, pady=15)
		self.key_file_lbl.grid_remove()

		self.k_file = ttk.Label(self.window, text=self.key_file) #  font=('Lucida Console', 12), width = 30
		self.k_file.grid(column=1, row=2, padx=30, pady=15)
		self.k_file.grid_remove()

		self.ext_btn = ttk.Button(self.window, text='Extract', command=self.ext_btn_clicked, takefocus=False)  # bg = ('#4e92df'), width = 10
		self.ext_btn.grid(column=2, row=3, padx=0, pady=15)
		self.ext_btn.grid_remove()

		self.window.mainloop()

	def dec_file_y(self):
		self.encrypt = True
		self.sel_key_file.grid()
		self.sel_key_file_btn.grid()

	def dec_file_n(self):
		self.encrypt = False
		self.ext_btn.grid()
		self.sel_key_file.grid_remove()
		self.sel_key_file_btn.grid_remove()


	def sel_key_file_btn_clicked(self):
		
		self.key_file = filedialog.askopenfilename(filetypes=(('Key files', '*.bin'),), initialdir=os.getcwd())
		self.root.key_file = self.key_file

		self.key_file_lbl.grid()
		self.k_file.grid()
		self.k_file.config(text=self.key_file)


		if self.key_file == '':
			messagebox.showinfo('Error!','Selected key file does not exist!')
			self.ext_btn.grid_remove()
		else:
			self.ext_btn.grid()

		self.window.lift()

	def ext_btn_clicked(self):

		try:
			extract_pptx = EmbedExtract(self.root.pptx_file)
		except PackageNotFoundError as e:
			messagebox.showinfo('Error!', 'Selected PowerPoint file does not exist!')
			self.window.destroy()
		else:
			hex_strings = extract_pptx.extract_hex()

			if self.encrypt is None:
				messagebox.showinfo('Error!','Please select whether embedded file was encrypted!')
			elif self.encrypt:

				with open(self.key_file, 'rb') as keyfile:
					key = keyfile.read()

				try:
					EncoderDecoder.decode_to_file(hex_strings, decryption=self.encrypt, key=key)
				except ValueError as err:
					messagebox.showinfo('Error!', str(err))
					self.window.destroy()
				else:
					messagebox.showinfo('Success!', 'Successfully extracted hidden file from selected cover PowerPoint file!\nHiddle file is saved in output folder.')
					self.window.destroy()
				
			else:
				try:
					EncoderDecoder.decode_to_file(hex_strings)
				except ValueError as err:
					messagebox.showinfo('Error!', str(err))
					self.window.destroy()
				else:
					messagebox.showinfo('Success!', 'Successfully extracted hidden file from selected cover PowerPoint file!\nHiddle file is saved in output folder.')
					self.window.destroy()
		





def main():
	"""This is the main function.
	If this module is executed as a script, execution will commence in this function.
	"""
	MainGUI()

if __name__ == '__main__':
	main()