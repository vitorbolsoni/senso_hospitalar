import tkinter as tk
from internacao import JanelaInternacao
from uti import JanelaUti


class JanelaMenu:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.iconbitmap(tk.PhotoImage('unimed.ico'))
        self.janela.title('Senso Hospitalar')
        self.fundo = tk.Frame(self.janela, background='#EB4E1C')
        self.fundo.pack()

        px = 2
        py = 2
        fg = '#009'
        bg = '#dde'

        self.fechar = tk.Button(self.fundo, text='Sair', command=self.janela.destroy)
        self.fechar.pack(side='bottom', anchor='se', fill='none', padx=px, pady=py)

        self.internacao = tk.Button(self.fundo, text='Internação', command=JanelaInternacao)
        self.internacao.pack(side='bottom', anchor='sw', fill='none', padx=px, pady=py)
        self.uti = tk.Button(self.fundo, text="UTI's", command=JanelaUti)
        self.uti.pack(side='bottom', anchor='sw', fill='none', padx=px, pady=py)

        arquivo_logo = tk.PhotoImage(file='logo_unimed.png')
        self.logo = tk.Label(self.fundo, image=arquivo_logo, background=bg)
        self.logo.pack(side='left', anchor='nw', padx=px, pady=py)

        self.status = tk.Label(self.fundo, text='teste status', background=bg)
        self.status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

        self.instituicao = tk.Label(self.fundo, text='Unimed Noroeste Capixaba', foreground=fg, background=bg)
        self.instituicao.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.titulo = tk.Label(self.fundo, text='Senso Hospitalar', font=('Copperplate', 14), foreground=fg, background=bg)
        self.titulo.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.cabecalho = tk.Label(self.fundo, text='Menu Principal', font=('Copperplate', 11), foreground=fg, background=bg)
        self.cabecalho.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.janela.mainloop()


menu = JanelaMenu()
