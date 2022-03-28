import tkinter as tk


class JanelaInternacao(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

    def fundo(self, bg='#EB4E1C'):
        fundo = tk.Frame(self, borderwidth=2, background=bg)
        fundo.place(width=1000, height=1000)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho, py=2, bg='#dde'):
        instituicao = tk.Label(self, text=nome_instituicao, foreground='#009', background=bg)
        instituicao.pack(side='top', anchor='center', fill='none', padx=2, pady=py)
        titulo = tk.Label(self, text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background=bg)
        titulo.pack(side='top', anchor='center', fill='none', padx=2, pady=py)
        cabecalho = tk.Label(self, text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background=bg)
        cabecalho.pack(side='top', anchor='center', fill='none', padx=2, pady=py)

    def logo(self, arquivo, py=2, bg='#dde'):
        logo = tk.Label(self, image=arquivo, background=bg)
        logo.pack(side='left', anchor='nw', fill='none', padx=2, pady=py)

    def status(self, bg='#dde'):
        status = tk.Label(self, text='teste status', background=bg)
        status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

    def tabela(self, py=20, cor_letra='#009'):
        ind_setor = tk.Label(self, text='Setores', foreground=cor_letra)
        ind_setor.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_leitos = tk.Label(self, text='Total de Leitos', foreground=cor_letra)
        ind_leitos.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_ocupacao = tk.Label(self, text='Ocupação', foreground=cor_letra)
        ind_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_perc_ocupacao = tk.Label(self, text='% Ocupação', foreground=cor_letra)
        ind_perc_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_altastransf = tk.Label(self, text='''Altas ou
Transferências Internas''', foreground=cor_letra)
        ind_altastransf.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_prev_alta = tk.Label(self, text='''Previsão de
Alta Para Amanhã''', foreground=cor_letra)
        ind_prev_alta.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        ind_obito = tk.Label(self, text='Óbitos', foreground=cor_letra)
        ind_obito.pack(side='left', anchor='n', fill='none', padx=2, pady=py)


def abre_janela_internacao():
    root = tk.Toplevel()
    internacao = JanelaInternacao(root)
    internacao.fundo()
    arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')
    internacao.logo(arquivo_logo)
    internacao.status()
    internacao.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')
    internacao.tabela()
    root.mainloop()
