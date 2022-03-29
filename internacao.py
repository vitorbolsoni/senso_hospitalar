import tkinter as tk


class JanelaInternacao:
    def __init__(self):
        self.janela = tk.Toplevel()
        self.janela.focus_force()
        self.janela.grab_set()
        self.janela.iconbitmap(tk.PhotoImage('unimed.ico'))
        self.janela.title('Senso Hospitalar - Internação')
        self.fundo = tk.Frame(self.janela, background='#EB4E1C')
        self.fundo.pack()

        px = 2
        py = 2
        fg = '#009'
        bg = '#dde'

        # self.setor = tk.Label(self.fundo, text=setor, foreground='#255')
        # self.setor.place(x=125, y=150)
        # self.leitos = tk.Label(self.fundo, text=leitos, foreground='#255')
        # self.leitos.place(x=210, y=150)
        # self.ocupacao = tk.Label(self.fundo, text=ocupacao, foreground='#255')
        # self.ocupacao.place(x=285, y=150)
        # self.perc_ocupacao = tk.Label(self.fundo, text=perc_ocupacao, foreground='#255')
        # self.perc_ocupacao.place(x=360, y=150)
        # self.altas_transf = tk.Label(self.fundo, text=altas_transf, foreground='#255')
        # self.altas_transf.place(x=465, y=150)
        # self.prev_alta = tk.Label(self.fundo, text=prev_alta, foreground='#255')
        # self.prev_alta.place(x=585, y=150)
        # self.obito = tk.Label(self.fundo, text=obitos, foreground='#255')
        # self.obito.place(x=660, y=150)

        self.fechar = tk.Button(self.fundo, text='Fechar', command=self.janela.destroy)
        self.fechar.pack(side='bottom', anchor='se', fill='none', padx=px, pady=py)

        arquivo_logo = tk.PhotoImage(file='logo_unimed.png')
        self.logo = tk.Label(self.fundo, image=arquivo_logo, background=bg)
        self.logo.pack(side='left', anchor='nw', fill='none', padx=2, pady=py)

        self.status = tk.Label(self.fundo, text='teste status', background=bg)
        self.status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

        self.titulo = tk.Label(self.fundo, text='Senso Hospitalar', font=('Copperplate', 14), foreground=fg, background=bg)
        self.titulo.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.cabecalho = tk.Label(self.fundo, text='Internação', font=('Copperplate', 11), foreground=fg, background=bg)
        self.cabecalho.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.indice_setor = tk.Label(self.fundo, text='Setores', foreground=fg)
        self.indice_setor.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_leitos = tk.Label(self.fundo, text='Total de Leitos', foreground=fg)
        self.indice_leitos.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_ocupacao = tk.Label(self.fundo, text='Ocupação', foreground=fg)
        self.indice_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_perc_ocupacao = tk.Label(self.fundo, text='% Ocupação', foreground=fg)
        self.indice_perc_ocupacao.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_altastransf = tk.Label(self.fundo, text='''Altas ou
Transferências Internas''', foreground=fg)
        self.indice_altastransf.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_prev_alta = tk.Label(self.fundo, text='''Previsão de
Alta Para Amanhã''', foreground=fg)
        self.indice_prev_alta.pack(side='left', anchor='n', fill='none', padx=2, pady=py)
        self.indice_obito = tk.Label(self.fundo, text='Óbitos', foreground=fg)
        self.indice_obito.pack(side='left', anchor='n', fill='none', padx=2, pady=py)

        self.janela.mainloop()
