import tkinter as tk


class Figura:
	INDICE, COL, FIL = 0, 0, 0
	RANGO=10
	def __init__(self, char='*', esp='_'):
		self.esp, self.char = esp, char
		self.pos = (
			((0,0),(1,0),(1,1),(1,2)), ((0,2),(0,1),(1,1),(2,1)),
			((2,2),(1,2),(1,1),(1,0)), ((2,0),(2,1),(1,1),(0,1))
		)
		
	def dibuja(self):
		self.rango()
		for f, c in self.pos[self.INDICE]:
			self.mz[self.FIL+f][self.COL+c] = self.char
			
	def rango(self):
		self.mz = [[self.esp]*self.RANGO for x in range(self.RANGO)]
		
	def gira(self):
		if self.COL<8 and self.COL>-1 and self.FIL<8:
			if self.INDICE<3:
				self.INDICE+=1
			else:
				self.INDICE=0
			self.dibuja()
		
	def der(self):
		n = 2 if self.INDICE==3 else 3
		if self.COL<self.RANGO-n:
			self.COL+=1
			
	def izq(self):
		limite = -1 if self.INDICE==1 else 0
		if self.COL>limite:
			self.COL-=1
			
	def baja(self):
		n = 2 if self.INDICE==0 else 3
		if self.FIL<self.RANGO-n:
			self.FIL+=1

	def restaura(self):
		self.FIL, self.COL = 0, 0
		self.INDICE = 0
		self.dibuja()
			

class TetrisFigura(tk.Tk):
	def __init__(self, **kw):
		super().__init__(**kw)
		self.geometry('200x220')
		self.figura = Figura(esp='🔲',char='🔳')
		fo = ('Segoe Ui', 12, 'bold')
		self.txt = tk.Text(self, bg='black', fg='gray', font=fo)
		self.txt.pack(fill='both', expand=1)
		self.acceso()
		self.muestra()
		self.title('Tetris')
		
	def acceso(self):
		d = {'<Left>':self.izq, '<Right>':self.der, '<Down>':self.baja,
			'<space>':self.restaura, '<Up>':self.gira}
		for c, v in d.items():
			self.bind(c,v)
			
	def muestra(self):
		self.txt.delete('1.0', 'end')
		self.figura.dibuja()
		for fila in self.figura.mz:
			self.txt.insert('end', f"{''.join(fila)}\n")
		self.txt.tag_configure('ct', justify='center')
		self.txt.tag_add('ct', '1.0', 'end')
		
	def izq(self, e):
		self.figura.izq()
		self.muestra()
		
	def der(self, e):
		self.figura.der()
		self.muestra()

	def baja(self, e):
		self.figura.baja()
		self.muestra()

	def gira(self, e):
		self.figura.gira()
		self.muestra()

	def restaura(self, e):
		self.figura.restaura()
		self.muestra()
		
		
if __name__=="__main__":
	vn = TetrisFigura()
	vn.mainloop()