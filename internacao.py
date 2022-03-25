import tkinter as tk


class App(tk.Frame):
    def __init__(self):
        super().__init__()

    def configurar(self, borda, cor_fundo):
        tk.Frame(self, borderwidth=borda, background=cor_fundo)


class Fundo(App):
    def __init__(self):
        super().__init__()


class Topo(Fundo):
    def __init__(self):
        super().__init__()

    def logo(self, arquivo):
        logo = tk.Label(image=arquivo, background='#dde')
        logo.grid(column=10, row=10, ipady=2)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho):
        instituicao = tk.Label(text=nome_instituicao, foreground='#009', background='#dde')
        instituicao.grid(column=40, row=10, ipady=5)
        titulo = tk.Label(text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background='#dde')
        titulo.grid(column=40, row=11, ipady=5)
        cabecalho = tk.Label(text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background='#dde')
        cabecalho.grid(column=40, row=12, ipady=5)


app = App()
app.configurar(2, '#7C8428')
arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')

topo = Topo()
topo.logo(arquivo_logo)
topo.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')

app.mainloop()
