import tkinter as tk
from internacao import abre_janela_internacao
from uti import abre_janela_uti


class Janela:
    def __init__(self):
        px = 2
        py = 2
        bg = '#dde'
        texto_cabecalho = 'Menu Principal'
        # arquivo_logo = 'logo_unimed_init.png'
        self.janela = tk.Tk()
        # self.janela.iconbitmap('logo_unimed_init.ico')
        self.janela.title('Senso Hospitalar')
        self.fundo = tk.Frame(self.janela, background='#EB4E1C')
        self.fundo.pack()

        self.instituicao = tk.Label(self.fundo, text='Unimed Noroeste Capixaba', foreground='#009', background=bg)
        self.instituicao.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.titulo = tk.Label(self.fundo, text='Senso Hospitalar', font=('Copperplate', 14), foreground='#009', background=bg)
        self.titulo.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        self.cabecalho = tk.Label(self.fundo, text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background=bg)
        self.cabecalho.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

        # self.logo = tk.Label(self.janela, image=arquivo_logo, background=bg)
        # self.logo.pack(side='left', anchor='nw', fill='none', padx=px, pady=py)

        self.status = tk.Label(self.fundo, text='teste status', background=bg)
        self.status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

        self.fechar = tk.Button(self.fundo, text='Sair', command=self.janela.destroy)
        self.fechar.pack(side='bottom', anchor='se', fill='none', padx=px, pady=py)

        self.internacao = tk.Button(self.fundo, text='Internação', command=abre_janela_internacao)
        self.internacao.pack(side='bottom', anchor='sw', fill='none', padx=px, pady=py)
        self.uti = tk.Button(self.fundo, text="UTI's", command=abre_janela_uti)
        self.uti.pack(side='bottom', anchor='sw', fill='none', padx=px, pady=py)

        self.janela.mainloop()


menu = Janela()
