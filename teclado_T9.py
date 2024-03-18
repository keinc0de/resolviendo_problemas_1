import tkinter as tk
from tkinter import ttk


class Letras:
	def __init__(self, indice=0, num=0):
		letras = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
		self.i = indice
		self.letras = letras[num]
		
	def mueve_indice(self):
		limite = len(self.letras)-1
		if self.i<limite:
			self.i += 1
		else:
			self.i = 0
		
	def obten(self):
		letra = self.letras[self.i]
		self.mueve_indice()
		return letra


class Gui(tk.Tk):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.geometry('250x210')
		self._inicia_botones()
		s = ttk.Style()
		s.theme_use('clam')
		s.configure('TButton', font=('Consolas', 12))
		self.title('Teclado T9')
		
	def _inicia_botones(self):
		fm = tk.Frame(self)
		fm.grid(row=0, column=0, columnspan=3, sticky='wens')
		fm.columnconfigure(0, weight=1)
		fm.rowconfigure(0, weight=1)
		self.var_texto = tk.StringVar()
		ops = {'font':('Consolas', 14, 'bold')}
		ent = tk.Entry(fm, textvariable=self.var_texto, **ops)
		ent.grid(row=0, column=0, sticky='wens')
		self.var_letra = tk.StringVar()
		enl = tk.Entry(fm, textvariable=self.var_letra, width=4, fg='gray', **ops)
		enl.grid(row=0, column=1, sticky='wens')
		btx = ttk.Button(fm, text='X', width=3, command=self.borrar, takefocus=False)
		btx.grid(row=0, column=2, sticky='wens')
		
		self.rowconfigure((0,1,2,3), weight=1)
		self.columnconfigure((0,1,2), weight=1)
		bt1 = ttk.Button(self, takefocus=False, command=self.agrega_uno)
		bt1.grid(row=1, column=0, sticky='wens')
		self.bts = []
		self.iconos = []
		indices = ((1,1),(1,2), (2,0),(2,1),(2,2), (3,0),(3,1),(3,2))
		for x, i in enumerate(indices):
			r,c = i			
			bt = self.boton(x)
			self.bts.append(bt)
			bt.grid(row=r, column=c, sticky='wens')
		self.bind('<Button-3>', self.muestra_texto)
		
		ico1 = self.ico('1')
		self.iconos.append(ico1)
		bt1.config(image=ico1)
		ico_t9 = self.ico('t9')
		self.iconos.append(ico_t9)
		self.iconphoto(True, ico_t9)
		
	def boton(self, num):
		lt = Letras(num=num)
		numero = num+2
		letras = lt.letras
		lt.letras = str(numero)+letras
		ico = self.ico(str(numero))
		self.iconos.append(ico)
		cmd = lambda: self.var_letra.set(lt.obten())
		bt = ttk.Button(self, text=letras, command=cmd, image=ico, compound='left', takefocus=False)
		return bt
		
	def muestra_texto(self, e=None):
		letra = self.var_letra.get()
		texto = self.var_texto.get()
		texto += letra
		self.var_texto.set(texto)
		
	def agrega_uno(self):
		texto = self.var_texto.get()
		texto += str(1)
		self.var_texto.set(texto)
		
	def borrar(self):
		texto = self.var_texto.get()
		txt = texto[:-1] if texto else ''
		self.var_texto.set(txt)
		
	def ico(self, nom):
		d = {
			'1':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAiklEQVR4nGNgGGjAiFVUq6Ceg
			ZGhAUXs//8whmsTV6MrZcJhrDaayCcGBoZH2JRiN+DqhDAGBgZk2/gYGBjkiDeAgYGB4T/DVZxyRBmA6
			Q0SDUAFJIYBJiAjDIgENApE9RwpBgaGVBQxRsZQ4g1gZkllYGSQRhMNZdDKxzAEhxf+X8MiiDMmBhYAA
			BFnF1vkHJLNAAAAAElFTkSuQmCC''',
			'2':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAhklEQVR4nGNgGGjACGdpFdQzM
			DI0EFD/ieH/fzeGaxNPwgSYqOcCbEC9jJeB+ddOBkYGS/JccLPrMwMjwxN8SljgLK38UAZGxlWEnIwOk
			FzAqEWqZlQXoIP/DA0M1yY0kuAC8gAVo5GYQPzPcJzhL5s7w82uz+S5gJFBm4H5J0pgU+yFgQcAK04f0
			jW7KDIAAAAASUVORK5CYII=''',
			'3':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAw0lEQVR4nMWRwQ2CQBBF3yiJJ
			y1ACyChAI1WYANShQmevGoJHrzZATaAFqAVaGIBWASBrAdEEHHQE/+0O/vnz5+/0DTkdXK8ESJHoKfw9
			1w2brHQKmhNa5rBMMGe978IlMnGJY4HGEJNU7RH7GWXdnRAGD8dhCTxkNv2nlGsjybHmyHip5dI1Qdth
			SoIp+L0tKThzQ2VK+gOkk6A4axR8gycxQphnU8zLgmBOoCqEDOI+Fh/hWiutWxV4Id9gV35F5rHAxf7N
			mZZvBMQAAAAAElFTkSuQmCC''',
			'4':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAnElEQVR4nGNgGGjACGdpFdQzM
			DI0wPn/GRoYrk1oZNAuWMXAwBAKFf3E8P+/G8O1iSdhypgQZv2/hmG8ehkvw38GGXwuQDKAUQtD9mbXZ
			wZGhidIrvrM8PfvYxwGoIP/1zBcwMjAy8DMLEukAVhcgAXgMQCLl/AbgBaIjAwNDNoF/xkQMUDIAOJsR
			AeMBFUQnw7IA3Q2AEtCGngAAEhwL1YSipbXAAAAAElFTkSuQmCC''',
			'5':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAoklEQVR4nGNgGGjACGdpFdQzM
			DI0EFD/ieH/fzeGaxNPwgSYKHUBC06Z/wwNDNcmNBIygGIXkBYG/xmeMvz9Y8Zwc8oz8lzAyMDLwMwsi
			90F2IB6GS8D86+dDIwMllAR6scCaQb8Z/jM8PfvY2QhRDSql/EysPy0YmBgTGZgYAiFCP5CNQARBs8wD
			WD+VcTAwNhAkosYULzw/xpB1Vi8MPAAANBBLMGu7o0dAAAAAElFTkSuQmCC''',
			'6':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAfElEQVR4nGNgGGjACGdpFdQzM
			DI0EFD/ieH/fzeGaxNPwgSYKHUBCx651QxXJ4QRMgC3C/4zXCXGBUhhkB/KwMi4ioB6fGHAqEWMjegAn
			xcaGK5OYGRgYFhNngEUu4Dh/zViDECKxv/XkMOUgZFxFYN2ASUuIA5QbMDAAwAAbxsClHQGdAAAAABJR
			U5ErkJggg==''',
			'7':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAZ0lEQVR4nGNgGGjACGdp5ZszM
			DLuYmBg4MOr4z9DA8O1CY0wLhOlLmCBs65NPMnAwMCPoUKroJ6BkaEBlwEUu4AIA/5fo9AAil1AsQGMW
			hQagBYGjAzaJBqAbh7DVcoMQAMUGzDwAAAC+w7INcjDJAAAAABJRU5ErkJggg==''',
			'8':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAzUlEQVR4nMWSuw3CQBBE32Hkk
			AaQKMAuwB1ABZRAbEogdmBkiS6oAIjBIgdLjvkUgCMkTkuAQCeDj6/ERKfZudnZ24N/Q91OXhig1BRoV
			KqFFO12yKPiStWMcst6+dLOxzl6JmUYKK8kH3NyGwipzbNWWRHW5FGBYmtwBVpvKgwkK8Ud4PcF6L6WQ
			Os5ws4mRrEgH+0fGzj1HoqmETdFSRs4GPoOXhhUjFCGDFklM2BiC2UxuNvKmwZvP+KHMLbgxs8+DUJMl
			iy/bfpbnAE0QTXV6f7SbAAAAABJRU5ErkJggg==''',
			'9':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAn0lEQVR4nGNgGGjACGdpFdQzM
			DI0EFD/ieH/fzeGaxNPwgSYKHUBbgP+MzQw/GHjY/jPcJw8AxgYGBhudn1mYGR4gmToZ4a/fx8TZwAjQ
			wODdsF/BgaGUCQxXgZmZlniXUAEYMQrq17Gy8D8aycDI4MlVITCWCApDLABLGHAgnBujhQDM8spBkYGa
			YT0L4JmIlzAzJKKqpk4QHEYDDwAAA7EKwQoq1cvAAAAAElFTkSuQmCC''',
			't9':'''iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAlElEQVR4nJ2T0Q2AIAxEH0aN
			LCAruKEzuKEryAIa/fFDSSoSxF7CD1yvvV4wwIIezgDLPjV9jtWOh1/n7sGxw+YBKm3rIKgWCDCIHUgr
			7Xj4XGe4bFSAu0+SLAqSnD8WkmnVJZVxAsUThKhy+JrA2WF7jB5PU2JBLu+1hy8BWZBMISsQZa5PIRaT
			UKcQ3oy403xrdwLtky8YFwbiFgAAAABJRU5ErkJggg==''',
		}
		return tk.PhotoImage(data=d.get(nom))
		
		
if __name__=='__main__':
	app = Gui()
	app.mainloop()