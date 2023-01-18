import tkinter


# ---------------------------------------------------------------------------------------------------------------------
def linha(x):
    linha1 = tkinter.Label(janela, text="-"*100)
    linha1.place(x=10, y=x)


# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Conhecimento')

largura_janela = 530
altura_janela = 800

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posl = float(largura_janela/2 - largura_tela/2)
posa = float(altura_janela/2 - altura_tela/2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posl, posa))
janela.resizable(width=False, height=False)
# 1--------------------------------------------------------------------------------------------------------------------
variavel = str('')
vardica = tkinter.StringVar()

vardica.set(f'1: Para saber o tipo de uma variavél \"type(variavel)\" = {type(variavel)}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12))
dica.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------------------------
linha(30)
# 2--------------------------------------------------------------------------------------------------------------------
n1 = int(1)
n2 = int(2)
vardica = tkinter.StringVar()

vardica.set(f'2: Misturando frases com variáveis {n1} + {n2} = {n1+n2}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12))
dica.place(x=10, y=50)
# ---------------------------------------------------------------------------------------------------------------------
linha(70)
# 3--------------------------------------------------------------------------------------------------------------------
num = str(1)
texto = str('um')
vardica = tkinter.StringVar()

teste1 = num.isnumeric()
teste2 = texto.isnumeric()
vardica.set(f'3: Teste de strings: {teste1} e {teste2}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12))
dica.place(x=10, y=90)
# ---------------------------------------------------------------------------------------------------------------------
linha(110)
# 4--------------------------------------------------------------------------------------------------------------------
texto = '''
soma: 5 + 2 = 7
subtração: 5 - 2 = 3
multiplicação: 5 * 2 = 10
divisão: 5 / 2 = 2.5
Potencia: 5 ** 2 = 25
Divisao inteira: 5 // 2 = 2
Resto da divisao: 5 % 2  = 1
raiz quadrada: 9**(1/2) = 3
raiz cubica: 125**(1/3) = 5
multiplicando strings: 'oi'*10)

'''

vardica = tkinter.StringVar()
vardica.set(texto)

vardica.set(f'4: Operadores:\n {texto}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12), justify='left')
dica.place(x=10, y=130)
# ---------------------------------------------------------------------------------------------------------------------
linha(350)
# 5--------------------------------------------------------------------------------------------------------------------
texto = '''
nome = 'thayron'
print(f'esquerda {nome:<20}') -> esquerda thayron
print(f'direita {nome:>20}') -> direita               thayron
print(f'centro {nome:^20}') -> centro         thayron
print(f'esquerda {nome:=<20}') -> esquerda thayron=============
print(f'direita {nome:=>20}') -> direita  =============thayron
print(f'centro {nome:=^20}') -> centro   ======thayron=======
end=(' ') mantem na mesma linha \n quebra a linha
'''

vardica = tkinter.StringVar()
vardica.set(texto)

vardica.set(f'4: Formatando prints:\n {texto}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12), justify='left')
dica.place(x=10, y=370)
# ---------------------------------------------------------------------------------------------------------------------
linha(575)
# 5--------------------------------------------------------------------------------------------------------------------
texto = '''
n1 = int(5)
n2 = int(2)

if n1 % n2 == 0:
    print(f'a divisão é {n1 / n2:.0f}')
else:
    print(f'a divisão é {n1 / n2:.2f}')
'''
vardica = tkinter.StringVar()
vardica.set(texto)

vardica.set(f'5: Teste de número inteiro e formatação de número:\n {texto}')

dica = tkinter.Label(janela, textvariable=vardica, font=('', 12), justify='left')
dica.place(x=10, y=595)

janela.mainloop()
