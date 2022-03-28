import tkinter as tk


class Janela(tk.Frame):
    def __init__(self, master, setor, leitos, ocupacao, perc_ocupacao, altas_transf, prev_alta, obitos):
        super().__init__(master)
        self.setor = tk.Label(self, text=setor, foreground='#255')
        self.setor.place(x=125, y=150)
        self.leitos = tk.Label(self, text=leitos, foreground='#255')
        self.leitos.place(x=210, y=150)
        self.ocupacao = tk.Label(self, text=ocupacao, foreground='#255')
        self.ocupacao.place(x=285, y=150)
        self.perc_ocupacao = tk.Label(self, text=perc_ocupacao, foreground='#255')
        self.perc_ocupacao.place(x=360, y=150)
        self.altas_transf = tk.Label(self, text=altas_transf, foreground='#255')
        self.altas_transf.place(x=465, y=150)
        self.prev_alta = tk.Label(self, text=prev_alta, foreground='#255')
        self.prev_alta.place(x=585, y=150)
        self.obito = tk.Label(self, text=obitos, foreground='#255')
        self.obito.place(x=660, y=150)
        self.pack()

    def fundo(self):
        self.config(background='#6DA0FA')

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho, py=2, bg='#6DA0FA'):
        instituicao = tk.Label(self, text=nome_instituicao, foreground='#009', background=bg)
        instituicao.pack(side='top', anchor='center', fill='none', padx=2, pady=py)
        titulo = tk.Label(self, text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background=bg)
        titulo.pack(side='top', anchor='center', fill='none', padx=2, pady=py)
        cabecalho = tk.Label(self, text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background=bg)
        cabecalho.pack(side='top', anchor='center', fill='none', padx=2, pady=py)

    def logo(self, arquivo, py=2, bg='#6DA0FA'):
        logo = tk.Label(self, image=arquivo, background=bg)
        logo.pack(side='left', anchor='nw', fill='none', padx=2, pady=py)

    def status(self, bg='#dde'):
        status = tk.Label(self, text='teste status', background=bg)
        status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

    def tabela(self, py=20, cor_letra='#009', bg='#6DA0FA'):
        indice_setor = tk.Label(self, text='Setores', foreground=cor_letra, background=bg)
        indice_setor.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_leitos = tk.Label(self, text='Total de Leitos', foreground=cor_letra, background=bg)
        indice_leitos.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_ocupacao = tk.Label(self, text='Ocupação', foreground=cor_letra, background=bg)
        indice_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_perc_ocupacao = tk.Label(self, text='% Ocupação', foreground=cor_letra, background=bg)
        indice_perc_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_altastransf = tk.Label(self, text='''Altas ou
Transferências Internas''', foreground=cor_letra, background=bg)
        indice_altastransf.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_prev_alta = tk.Label(self, text='''Previsão de
Alta Para Amanhã''', foreground=cor_letra, background=bg)
        indice_prev_alta.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        indice_obito = tk.Label(self, text='Óbitos', foreground=cor_letra, background=bg)
        indice_obito.pack(side='left', anchor='n', fill='none', padx=2, pady=py)

    def fechar(self, root, px=5, py=5):
        botao = tk.Button(self, text='Fechar', command=root.destroy)
        botao.pack(side='bottom', anchor='se', fill='none', padx=px, pady=py)


def abre_janela_internacao():
    root = tk.Toplevel()
    internacao = Janela(root, 'Clinica 1º', 50, 45, 90, 2, 3, 1)
    internacao.fundo()
    internacao.fechar(root)
    arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')
    internacao.logo(arquivo_logo)
    internacao.status()
    internacao.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária Internação')
    internacao.tabela()
    root.mainloop()
