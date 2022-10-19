from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

co0 = "#444466"  # preto
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#ef5350"  # vermelho

#### Janela ########

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#### Criando quadro ###
quadro_pokemon = Frame(janela, width=500, height=290, relief='flat')
quadro_pokemon.grid(row=1, column=0)

### nome ####
pok_nome = Label(quadro_pokemon, text='Jigglipuff', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

### Categoria ###
pok_tipo = Label(quadro_pokemon, text='Balão', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

### Identificação ###
pok_identificacao = Label(quadro_pokemon, text='#039', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1,
                          fg=co0)
pok_identificacao.place(x=12, y=75)

### imagem do Pokemon ###
imagem_pokemon = Image.open('images/jigglypuff.png')
imagem_pokemon = imagem_pokemon.resize((238, 238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imegem = Label(quadro_pokemon, image=imagem_pokemon, relief='flat', bg=co1, fg=co0)
pok_imegem.place(x=60, y=50)

pok_tipo.lift()

### Status ###
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Arial 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

### hp ###
pok_hp = Label(janela, text='HP: 115', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

### Ataque ###

pok_attack = Label(janela, text='Ataque: 45', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_attack.place(x=15, y=385)

### Defesa ###
pok_defesa = Label(janela, text='Defesa: 20', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

### Velocidade ###
pok_velocidade = Label(janela, text='Velocidade: 20', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

### Total ###
pok_total = Label(janela, text='Total: 180', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)




### Habilidades ###
pok_habilidade = Label(janela, text='Habilidade', relief='flat', anchor=CENTER, font=('Arial 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

### habilidade cute charme ###
pok_CC = Label(janela, text='Cute Charm', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_CC.place(x=195, y=360)

### habilidade competitive ###

pok_comptt = Label(janela, text='Competitive', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_comptt.place(x=195, y=385)


janela.mainloop()
