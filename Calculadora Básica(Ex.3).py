import tkinter as tk

# A função callback "escrever" verifica o texto do botão pressionado.
# O botão "CLEAR" limpa o texto em "screen" e o botão "ENTER" realiza a função "analisar"
# Outros botões acrescentam o seu texto ao "screen"
def escrever(texto_botao):
    if texto_botao == "CLEAR":
        screen.config(text= "")
        return
    elif texto_botao == "ENTER":
        analisar()
        return
    else:
        text = screen.cget("text")
        text += texto_botao
        screen.config(text= text)
        return

# A função "analisar" verifica se há texto no "screen" e realiza os cálculos existentes se for o caso
def analisar():
    texto = screen.cget("text")
    if texto == "":
        print("Nenhum input encontrado")
        return 
    resultado = eval(texto)
    screen.config(text= str(resultado))
    return

# Definição da janela de visualização
root = tk.Tk()  
root.title("Calculadora Básica")
root.minsize(350,500)

# Label que funciona como ecrã da calculadora
screen = tk.Label(root, text="",background="grey", fg="white", width=40, height=4, justify=tk.CENTER)
screen.pack(pady= 20)

# Frame para a primeira linha da calculadora. Contém os botões "CLEAR" e "/"
frame_linha1 = tk.Frame(root)
frame_linha1.pack()

botao_clear = tk.Button(frame_linha1, text= "CLEAR", command= lambda: escrever("CLEAR"), width= 29, height= 3)
botao_clear.config(background="light grey")
botao_clear.pack(side="left", padx= 8, pady= 15)

botao_div = tk.Button(frame_linha1, text= "/", command= lambda: escrever("/"), width= 7, height= 3)
botao_div.config(background="light grey")
botao_div.pack(side="left", padx= 8, pady= 15)


# Frame para a segunda linha da calculadora. Contém os botões "7", "8", "9" e "*"
frame_linha2 = tk.Frame(root)
frame_linha2.pack()

botao_7 = tk.Button(frame_linha2, text= "7", command= lambda: escrever("7"), width= 7, height= 3)
botao_7.config(background="light grey")
botao_7.pack(side="left", padx= 8, pady= 15)

botao_8 = tk.Button(frame_linha2, text= "8", command= lambda: escrever("8"), width= 7, height= 3)
botao_8.config(background="light grey")
botao_8.pack(side="left", padx= 8, pady= 15)

botao_9 = tk.Button(frame_linha2, text= "9", command= lambda: escrever("9"), width= 7, height= 3)
botao_9.config(background="light grey")
botao_9.pack(side="left", padx= 8, pady= 15)

botao_mult = tk.Button(frame_linha2, text= "*", command= lambda: escrever("*"), width= 7, height= 3)
botao_mult.config(background="light grey")
botao_mult.pack(side="left", padx= 8, pady= 15)


# Frame para a terceira linha da calculadora. Contém os botões "4", "5", "6" e "-"
frame_linha3 = tk.Frame(root)
frame_linha3.pack()

botao_4 = tk.Button(frame_linha3, text= "4", command= lambda: escrever("4"), width= 7, height= 3)
botao_4.config(background="light grey")
botao_4.pack(side="left", padx= 8, pady= 15)

botao_5 = tk.Button(frame_linha3, text= "5", command= lambda: escrever("5"), width= 7, height= 3)
botao_5.config(background="light grey")
botao_5.pack(side="left", padx= 8, pady= 15)

botao_6 = tk.Button(frame_linha3, text= "6", command= lambda: escrever("6"), width= 7, height= 3)
botao_6.config(background="light grey")
botao_6.pack(side="left", padx= 8, pady= 15)

botao_sub = tk.Button(frame_linha3, text= "-", command= lambda: escrever("-"), width= 7, height= 3)
botao_sub.config(background="light grey")
botao_sub.pack(side="left", padx= 8, pady= 15)


# Frame para a quarta linha da calculadora. Contém os botões "1", "2", "3" e "+"
frame_linha4 = tk.Frame(root)
frame_linha4.pack()

botao_1 = tk.Button(frame_linha4, text= "1", command= lambda: escrever("1"), width= 7, height= 3)
botao_1.config(background="light grey")
botao_1.pack(side="left", padx= 8, pady= 15)

botao_2 = tk.Button(frame_linha4, text= "2", command= lambda: escrever("2"), width= 7, height= 3)
botao_2.config(background="light grey")
botao_2.pack(side="left", padx= 8, pady= 15)

botao_3 = tk.Button(frame_linha4, text= "3", command= lambda: escrever("3"), width= 7, height= 3)
botao_3.config(background="light grey")
botao_3.pack(side="left", padx= 8, pady= 15)

botao_soma = tk.Button(frame_linha4, text= "+", command= lambda: escrever("+"), width= 7, height= 3)
botao_soma.config(background="light grey")
botao_soma.pack(side="left", padx= 8, pady= 15)


# Frame para a quinta linha da calculadora. Contém os botões "0" e "ENTER"
frame_linha5 = tk.Frame(root)
frame_linha5.pack()

botao_0 = tk.Button(frame_linha5, text= "0", command= lambda: escrever("0"), width= 7, height= 3)
botao_0.config(background="light grey")
botao_0.pack(side="left", padx= 8, pady= 15)

botao_enter = tk.Button(frame_linha5, text= "ENTER", command= lambda: escrever("ENTER"), width= 29, height= 3)
botao_enter.config(background="light grey")
botao_enter.pack(side="left", padx= 8, pady= 15)


root.mainloop() 


