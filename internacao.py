import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=1)


class Fundo(App):
    def __init__(self, master):
        super().__init__(master)
        master.pack_propagate(flag=True)

    def configurar(self, borda, cor_fundo):
        tk.Frame(self, borderwidth=borda, background=cor_fundo)


class Topo(Fundo):
    def __init__(self, master):
        super().__init__(master)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho):
        instituicao = tk.Label(text=nome_instituicao, foreground='#009', background='#dde')
        instituicao.place(x='500', bordermode='inside')
        titulo = tk.Label(text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background='#dde')
        titulo.place(bordermode='outside')
        cabecalho = tk.Label(text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background='#dde')
        cabecalho.place(anchor='center')

    def logo(self, arquivo):
        logo = tk.Label(image=arquivo, background='#dde')
        logo.place(anchor='nw')


janela = tk.Tk()
app = App(janela)
arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')

topo = Topo(app)
topo.configurar(2, '#7C8428')
topo.logo(arquivo_logo)
topo.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')

app.mainloop()
