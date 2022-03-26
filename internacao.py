import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()


class Fundo(App):
    def __init__(self, master):
        super().__init__(master)
        master = tk.Frame(self, borderwidth=2, background='#EB4E1C')
        master.place(width=1000, height=1000)


class Topo(Fundo):
    def __init__(self, master):
        super().__init__(master)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho):
        instituicao = tk.Label(self, text=nome_instituicao, foreground='#009', background='#dde')
        instituicao.pack(side='top', anchor='center', fill='none', padx=2, pady=2)
        titulo = tk.Label(self, text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background='#dde')
        titulo.pack(side='top', anchor='center', fill='none', padx=2, pady=2)
        cabecalho = tk.Label(self, text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background='#dde')
        cabecalho.pack(side='top', anchor='center', fill='none', padx=2, pady=2)

    def logo(self, arquivo):
        logo = tk.Label(self, image=arquivo, background='#dde')
        logo.pack(side='left', anchor='nw', fill='none', padx=2, pady=2)

    def status(self):
        status = tk.Label(self, text='teste status', background='#dde')
        status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)


class AbaJanela(Fundo):
    def __init__(self, master):
        super().__init__(master)

    def aba(self):
        ind_setor = tk.Label(self, text='Setores', foreground='#009')
        ind_setor.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_leitos = tk.Label(self, text='Total de Leitos', foreground='#009')
        ind_leitos.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_ocupacao = tk.Label(self, text='Ocupação', foreground='#009')
        ind_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_perc_ocupacao = tk.Label(self, text='% Ocupação', foreground='#009')
        ind_perc_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_altastransf = tk.Label(self, text='''Altas ou
Transferências Internas''', foreground='#009')
        ind_altastransf.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_prev_alta = tk.Label(self, text='''Previsão de
Alta Para Amanhã''', foreground='#009')
        ind_prev_alta.pack(side='left', anchor='n', fill='none', padx=2, pady=2)
        ind_obito = tk.Label(self, text='Óbitos', foreground='#009')
        ind_obito.pack(side='left', anchor='n', fill='none', padx=2, pady=2)


janela = tk.Tk()

app = App(janela)
fundo = Fundo(app)
topo = Topo(fundo)
arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')
topo.logo(arquivo_logo)
topo.status()
topo.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')
clinica = AbaJanela(app)
clinica.aba()

app.mainloop()
