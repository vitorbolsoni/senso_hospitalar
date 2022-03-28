import tkinter as tk
from internacao import abre_janela_internacao


class JanelaMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

    def fundo(self, bg='#EB4E1C'):
        fundo = tk.Frame(self, borderwidth=2, background=bg)
        fundo.place(width=1000, height=1000)

    def titulos(self, nome_instituicao, descricao_titulo, texto_cabecalho, px=2, py=2, bg='#dde'):
        instituicao = tk.Label(self, text=nome_instituicao, foreground='#009', background=bg)
        instituicao.pack(side='top', anchor='center', fill='none', padx=px, pady=py)
        titulo = tk.Label(self, text=descricao_titulo, font=('Copperplate', 14), foreground='#009', background=bg)
        titulo.pack(side='top', anchor='center', fill='none', padx=px, pady=py)
        cabecalho = tk.Label(self, text=texto_cabecalho, font=('Copperplate', 11), foreground='#009', background=bg)
        cabecalho.pack(side='top', anchor='center', fill='none', padx=px, pady=py)

    def logo(self, arquivo, px=5, py=2, bg='#dde'):
        logo = tk.Label(self, image=arquivo, background=bg)
        logo.pack(side='left', anchor='nw', fill='none', padx=px, pady=py)

    def status(self, bg='#dde'):
        status = tk.Label(self, text='teste status', background=bg)
        status.pack(side='right', anchor='ne', fill='none', padx=2, pady=2)

    def botoes(self, px=35, py=5):
        internacao = tk.Button(self, text='Internação', command=abre_janela_internacao)
        internacao.pack(side='bottom', anchor='sw', fill='none', padx=px, pady=py)


menu = JanelaMenu()

menu.fundo()
menu.botoes()
arquivo_logo = tk.PhotoImage(file='logo_unimed_init.png')
menu.logo(arquivo_logo)
menu.status()
menu.titulos('Unimed Noroeste Capixaba', 'Senso Hospitalar', 'Ocupação Diária dos Leitos')

menu.mainloop()
