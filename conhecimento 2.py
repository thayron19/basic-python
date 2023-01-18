import tkinter
import datetime


# ---------------------------------------------------------------------------------------------------------------------
def linha(x):
    linha1 = tkinter.Label(janela, text="-"*100)
    linha1.place(x=10, y=x)


# ---------------------------------------------------------------------------------------------------------------------
janela = tkinter.Tk()

janela.title('Cálculos')

largura_janela = 530
altura_janela = 630

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicaol = float(largura_janela/2 - largura_tela/2)
posicaoa = float(altura_janela/2 - altura_tela/2)

janela.geometry("%dx%d%d%d" % (largura_janela, altura_janela, posicaol, posicaoa))
janela.resizable(width=False, height=False)


# 1--------------------------------------------------------------------------------------------------------------------
def funcao_isnumber(teste_num):
    try:
        float(teste_num)
    except ValueError:
        return False
    return True


def funcao_calcular():
    teste_valor = porcentagem_valor_var.get().replace(',', '.')
    teste_porcento = porcentagem_var.get().replace(',', '.')

    if funcao_isnumber(teste_valor) and funcao_isnumber(teste_porcento):
        valor = float(teste_valor)
        porcento = float(teste_porcento)
        resultado = valor * porcento / 100

        valor_tratado = f'{valor:.2f}'.replace('.', ',')
        porcento_tratado = f'{porcento:.2f}'.replace('.', ',')
        resultado_tratado = f'{resultado:.2f}'.replace('.', ',')

        subtracao_tratado = f'{valor-porcento:.2f}'.replace('.', ',')
        soma_tratado = f'{valor+porcento:.2f}'.replace('.', ',')

        porcentagem_result_var.set(f'- - -  {resultado_tratado}  é  {porcento_tratado}%  de  {valor_tratado}')
        porcentagem_result_var1.set(f'- - -  {valor_tratado}  menos  {porcento_tratado}%  é  {subtracao_tratado}')
        porcentagem_result_var2.set(f'- - -  {valor_tratado}  mais  {porcento_tratado}%  é  {soma_tratado}')
    else:
        porcentagem_result_var.set('Valor errado')
        porcentagem_result_var1.set('')
        porcentagem_result_var2.set('')


porcentagem_texto = tkinter.Label(janela, text='Valor:', font=('', 12))
porcentagem_texto.place(x=10, y=10)

porcentagem_texto1 = tkinter.Label(janela, text='Porcentagem:', font=('', 12))
porcentagem_texto1.place(x=10, y=40)

porcentagem_valor_var = tkinter.StringVar()
porcentagem_valor_entry = tkinter.Entry(janela, textvariable=porcentagem_valor_var)
porcentagem_valor_entry.place(x=120, y=14)

porcentagem_var = tkinter.StringVar()
porcentagem_entry = tkinter.Entry(janela, textvariable=porcentagem_var)
porcentagem_entry.place(x=120, y=44)

porcentagem_btn = tkinter.Button(janela, text='Calcular', command=lambda: funcao_calcular())
porcentagem_btn.place(x=250, y=25)

linha(70)

porcentagem_result_var = tkinter.StringVar()
porcentagem_result_texto = tkinter.Label(janela, textvariable=porcentagem_result_var, font=('', 12))
porcentagem_result_texto.place(x=10, y=90)

porcentagem_result_var1 = tkinter.StringVar()
porcentagem_result_texto1 = tkinter.Label(janela, textvariable=porcentagem_result_var1, font=('', 12))
porcentagem_result_texto1.place(x=10, y=120)

porcentagem_result_var2 = tkinter.StringVar()
porcentagem_result_texto2 = tkinter.Label(janela, textvariable=porcentagem_result_var2, font=('', 12))
porcentagem_result_texto2.place(x=10, y=150)
# ---------------------------------------------------------------------------------------------------------------------
linha(170)


# 2--------------------------------------------------------------------------------------------------------------------
def funcao_tabuar():
    acumulado = ''

    if tabuada_var.get().isnumeric():
        numero = int(tabuada_var.get())

        for tabuada in range(11):
            acumulado += f'{tabuada} * {numero} = {tabuada * numero}\n'
        tabuada_result_var.set(acumulado)

    else:
        tabuada_result_var.set('Valor errado')


tabuada_texto = tkinter.Label(janela, text='Tabuada:', font=('', 12))
tabuada_texto.place(x=10, y=190)

tabuada_var = tkinter.StringVar()
tabuada_entry = tkinter.Entry(janela, textvariable=tabuada_var)
tabuada_entry.place(x=120, y=195)

tabuada_btn = tkinter.Button(janela, text='Tabuada', command=lambda: funcao_tabuar())
tabuada_btn.place(x=250, y=190)

tabuada_result_var = tkinter.StringVar()
tabuada_result_texto = tkinter.Label(janela, textvariable=tabuada_result_var, font=('', 12), justify='left')
tabuada_result_texto.place(x=10, y=225)
# ---------------------------------------------------------------------------------------------------------------------
linha(430)


# 3--------------------------------------------------------------------------------------------------------------------
def funcao_testeanobi():
    if anobi_var.get().isnumeric():
        ano = int(anobi_var.get())

        if ano == 0:
            ano = datetime.date.today().year

        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            anobiresult_var.set(f'{ano} é bissexto')
        else:
            anobiresult_var.set(f'{ano} não é bissexto')
    else:
        anobiresult_var.set('Valor errado')


anobi_texto = tkinter.Label(janela, text='Ano bissexto:', font=('', 12))
anobi_texto.place(x=10, y=450)

anobi_var = tkinter.StringVar()
anobi_entry = tkinter.Entry(janela, textvariable=anobi_var)
anobi_entry.place(x=120, y=455)

anobi_btn = tkinter.Button(janela, text='Teste ano \'0\'=ano atual', command=lambda: funcao_testeanobi())
anobi_btn.place(x=250, y=450)

anobiresult_var = tkinter.StringVar()
anobi_texto1 = tkinter.Label(janela, textvariable=anobiresult_var, font=('', 12))
anobi_texto1.place(x=10, y=480)
# ---------------------------------------------------------------------------------------------------------------------
linha(510)


# 4--------------------------------------------------------------------------------------------------------------------
def funcao_convert():
    if binario_var.get().isnumeric():
        x = int(binario_var.get())
        binresult.set(f'Binário: {bin(x)[2:]} \nOctal: {oct(x)[2:]} \nHexadecimal: {hex(x)[2:]}')
    else:
        binresult.set('Valor errado')


binconvert_texto = tkinter.Label(janela, text='Binário:', font=('', 12))
binconvert_texto.place(x=10, y=530)

binconvert_btn = tkinter.Button(janela, text='Teste ano \'0\'=ano atual', command=lambda: funcao_convert())
binconvert_btn.place(x=250, y=530)

binario_var = tkinter.StringVar()
binario_entry = tkinter.Entry(janela, textvariable=binario_var)
binario_entry.place(x=120, y=535)

binresult = tkinter.StringVar()
binresult_texto = tkinter.Label(janela, textvariable=binresult, font=('', 12), justify='left')
binresult_texto.place(x=10, y=560)
# ---------------------------------------------------------------------------------------------------------------------
janela.mainloop()
