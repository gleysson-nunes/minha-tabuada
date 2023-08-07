from customtkinter import *
from tkinter import messagebox

root = CTk()
root.geometry('400x433')
root.resizable(False, False)
root.title('Minha Tabuada')
root.iconbitmap('icone.ico')
root.configure(fg_color='#DAA520')

# Criação da Lista para armazenar todos os resultados das operações
resultados = []


def funcao():
    for resultado in resultados:    # Percorrendo toda a lista
        resultado.destroy()         # Excluindo todos os resultados da tela
    resultados.clear()              # Limpando a lista
    try:
        opcao = optionmenu.get()
        numero = int(entrynumero.get())
        if opcao == 'Adição':
            n = 0
            while n < 10:
                n += 1
                labelad = CTkLabel(root, text=f'{numero} + {n} = {numero + n}',
                                   font=('Arial', 17, 'bold'),
                                   text_color='#006400')
                labelad.pack()
                resultados.append(labelad)  # Adicionando o resultado na lista
        elif opcao == 'Subtração':
            n = 0
            while n < 10:
                n += 1
                labelsu = CTkLabel(root, text=f'{numero} - {n} = {numero - n}',
                                   font=('Arial', 17, 'bold'),
                                   text_color='#006400')
                labelsu.pack()
                resultados.append(labelsu)  # Adicionando o resultado na lista
        elif opcao == 'Multiplicação':
            n = 0
            while n < 10:
                n += 1
                labelmu = CTkLabel(root, text=f'{numero} x {n} = {numero * n}',
                                   font=('Arial', 17, 'bold'),
                                   text_color='#006400')
                labelmu.pack()
                resultados.append(labelmu)  # Adicionando o resultado na lista
        elif opcao == 'Divisão':
            n = 0
            while n < 10:
                n += 1
                resudiv = numero / n
                labeldiv = CTkLabel(root, text=f'{numero} ÷ '
                                               f'{n} = {resudiv:.2f}',
                                    font=('Arial', 17, 'bold'),
                                    text_color='#006400')
                labeldiv.pack()
                resultados.append(labeldiv)  # Adicionando o resultado na lista
        elif opcao == 'Potenciação':
            n = 0
            while n < 10:
                n += 1
                labelpot = CTkLabel(root, text=f'{numero} ** {n} = '
                                               f'{numero ** n}',
                                    font=('Arial', 17, 'bold'),
                                    text_color='#006400')
                labelpot.pack()
                resultados.append(labelpot)  # Adicionando o resultado na lista
    except ValueError:
        messagebox.showwarning(title='Aviso', message='O campo deve ser '
                                                      'preenchido com um '
                                                      'número inteiro')


entrynumero = CTkEntry(root, width=70, fg_color='#DAA520',
                       font=('Arial', 17, 'bold'),
                       text_color='#006400', justify='center')
entrynumero.pack(pady=12)

optionmenu = CTkOptionMenu(root, values=['Adição', 'Subtração',
                                         'Multiplicação', 'Divisão',
                                         'Potenciação'], anchor='center',
                           font=('Arial', 15, 'bold'), fg_color='#0000CD',
                           button_color='#0235BF',
                           button_hover_color='#0610B8',
                           dropdown_font=('Arial', 15, 'bold'),
                           dropdown_fg_color='#0235BF',
                           dropdown_hover_color='#0610B8')
optionmenu.pack(pady=10)

botao = CTkButton(root, text='Ver Tabuada', font=('Arial', 15, 'bold'),
                  fg_color='#0000CD', hover_color='#0610B8',
                  command=funcao)
botao.pack(pady=10)

root.mainloop()
