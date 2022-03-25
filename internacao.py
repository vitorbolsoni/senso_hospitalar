import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

class Fundo(App):
    def __init__(self, master):
        super().__init__(master)
        master = tk.Frame(self, borderwidth=2, background='#7C8428',)
        master.pack()


class Topo(Fundo):
    def __init__(self, master):
        super().__init__(master)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho):
        instituicao = tk.Label(text=nome_instituicao, foreground='#009', background='#dde')
        instituicao.pack(side='top', anchor='center', fill='none', padx=2, pady=2)
        titulo = tk.Label(text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background='#dde')
        titulo.pack(side='top', anchor='center', fill='none', padx=2, pady=2)
        cabecalho = tk.Label(text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background='#dde')
        cabecalho.pack(side='top', anchor='center', fill='none', padx=2, pady=2)

    def logo(self, arquivo):
        logo = tk.Label(image=arquivo, background='#dde')
        logo.pack(side='left', anchor='nw', fill='none', padx=2, pady=2)


janela = tk.Tk()
app = App(janela)
arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')
fundo = Fundo(app)
topo = Topo(fundo)
topo.logo(arquivo_logo)
topo.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')
app.mainloop()
