import string
import tkinter as tk


class CifradoCesar:
	def __init__(self):
		self.letras = list(string.ascii_uppercase)
		self.RAZON = 3
		
	def cambia(self, letra):
		letra = letra.upper()
		if letra in self.letras:
			i = self.letras.index(letra.upper())
			indice = self.indice(i)
			return self.letras[indice]
		else:
			return letra
		
	def indice(self, num):
		limite = len(self.letras)
		i = num+self.RAZON
		if i>=limite:
			i = (i-limite)-1
		return i
		
	def encode(self, palabras):
		texto = ''
		for letra in palabras:
			texto+=self.cambia(letra)
		return texto
		
	def decode(self, palabras):
		if self.RAZON>0:
			self.RAZON = -self.RAZON
		return self.encode(palabras)
		

class Ventana(tk.Tk):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.geometry('350x48')
		self.cc = CifradoCesar()	
		self.columnconfigure(1, weight=1)
		fo = ('Consolas', 9, 'bold')
		cf = {
			'fg':self.color('fg'), 'bg':self.color('bg'),
			'font':('Consolas', 8, 'bold'), 'relief':'flat'
		}
		lbe = tk.Label(self, text='ENCODE', **cf)
		lbe.grid(row=0, column=0)
		lbs = tk.Label(self, text='DECODE', **cf)
		lbs.grid(row=1, column=0)
		self.var_entrada = tk.StringVar()
		self.en_entrada = tk.Entry(self, textvariable=self.var_entrada)
		self.en_entrada.grid(row=0, column=1, sticky='we')
		self.var_salida = tk.StringVar()
		self.en_salida = tk.Entry(self, textvariable=self.var_salida)
		self.en_salida.grid(row=1, column=1, sticky='we')
		self.en_entrada.bind('<KeyPress>', self.encode)
		self.en_salida.bind('<KeyPress>', self.decode)
		btn = tk.Button(self, text='BORRAR', command=self.borrar)
		btn.grid(row=0, column=2, rowspan=2, sticky='wens')
		self.btn_config(btn)
		self.config(bg=self.color('bg'), pady=4)
		self.var_razon = tk.StringVar()
		self.en_rz = tk.Entry(self, textvariable=self.var_razon, width=3, font=('Consolas',16))
		self.en_rz.grid(row=0, column=3, sticky='wens', rowspan=2)
		self.var_razon.set(3)
		self.resizable(1, 0)
		self.title('Cifrado Cesar')
		ico = '''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAaUlEQVR4nGNkYGBg+PKS+z8
		DGYBH/CsjC7KAbFQTVoWPl9XhNISJkGZCgAWbID4bcbqAXIDVBTBATJiQ5QJkg/G6AD0ssLkIqwHoCom
		KRlJCHqcLyDFkYKKRYhcge5WRgYGy3EiOPhQAAMRdHzI0Vk0jAAAAAElFTkSuQmCC'''
		icono = tk.PhotoImage(data=ico)
		self.iconphoto(True, icono)
		
	def obten_razon(self):
		self.cc.RAZON = int(self.var_razon.get())
		
	def btn_config(self, btn):
		btn.config(
			fg=self.color('fg'), bg=self.color('bg'),
			font=('Consolas', 8, 'bold'), relief='flat',
			activebackground=self.color('bga'),
			#~ activeforeground=self.color('fga')
		)
			
	def color(self, nom):
		colores = {
			'bg':'#1B1D47', 'fg':'#FFC321',
			'bga':'orange', 'fga':'black'
		}
		return colores.get(nom, 'blue')
		
	def encode(self, e=None):
		self.obten_razon()
		tex = self.var_entrada.get()
		self.var_salida.set(self.cc.encode(tex))
		
	def decode(self, e=None):
		self.obten_razon()
		tex =self.var_salida.get()
		self.var_entrada.set(self.cc.decode(tex))
		
	def borrar(self):
		self.var_entrada.set('')
		self.var_salida.set('')
			
			
if __name__=="__main__":
	vn = Ventana()
	vn.mainloop()

	