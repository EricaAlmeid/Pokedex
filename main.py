from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from dados import*




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

def trocar_pokemon(i):
    global imagem_pokemon, pok_imegem

    ## Trocando a cor do fundo do pokemon ##

    quadro_pokemon['bg'] = pokemon[i]['tipo'][3]

    ##tipo de pokemon##
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_identificacao['text'] = pokemon[i]['tipo'][0]
    pok_identificacao['bg'] = pokemon[i]['tipo'][3]

    imagem_pokemon = pokemon[i]['tipo'][2]

    ### imagem do Pokemon ###
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imegem = Label(quadro_pokemon, image=imagem_pokemon, relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    pok_imegem.place(x=60, y=50)

    pok_tipo.lift()

    ## Status do pokemon ##
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_attack ['text'] = pokemon[i]['status'][1]
    pok_defesa ['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    ## Habilidades do pokemon##
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]



### nome ####
pok_nome = Label(quadro_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'),  fg=co1)
pok_nome.place(x=12, y=15)

### Categoria ###
pok_tipo = Label(quadro_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)

### Identificação ###
pok_identificacao = Label(quadro_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)

pok_identificacao.place(x=12, y=75)



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
pok_hb_1 = Label(janela, text='Cute Charm', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

### habilidade competitive ###

pok_hb_2 = Label(janela, text='Competitive', relief='flat', anchor=CENTER, font=('Arial 10'), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)

### Botao 1 ###

imagem_pok_1 = Image.open('images/cabeca_jigglypuff.png')
imagem_pok_1 = imagem_pok_1.resize((40, 40))
imagem_pok_1 = ImageTk.PhotoImage(imagem_pok_1)

b_pok_1 = Button(janela, command=lambda: trocar_pokemon('JigglyPuff'), image=imagem_pok_1, text='JigglyPuff', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

### Botao 2 ###

imagem_pok_2 = Image.open('images/cabeca-pikachu.png')
imagem_pok_2 = imagem_pok_2.resize((40, 40))
imagem_pok_2 = ImageTk.PhotoImage(imagem_pok_2)

b_pok_2 = Button(janela,  command=lambda: trocar_pokemon('Pikachu'), image=imagem_pok_2, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)


### Botao 3 ###

imagem_pok_3 = Image.open('images/cabeca-bulbasaur.png')
imagem_pok_3 = imagem_pok_3.resize((40, 40))
imagem_pok_3 = ImageTk.PhotoImage(imagem_pok_3)

b_pok_3 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'), image=imagem_pok_3, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

### Botao 4 ###

imagem_pok_4 = Image.open('images/cabeca-charmander.png')
imagem_pok_4 = imagem_pok_4.resize((40, 40))
imagem_pok_4 = ImageTk.PhotoImage(imagem_pok_4)

b_pok_4 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pok_4, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)


### Botao 5 ###

imagem_pok_5 = Image.open('images/cabeca-gyarados.png')
imagem_pok_5 = imagem_pok_5.resize((40, 40))
imagem_pok_5 = ImageTk.PhotoImage(imagem_pok_5)

b_pok_5 = Button(janela, command=lambda: trocar_pokemon('Gyarados'), image=imagem_pok_5, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

### Botao 6 ###

imagem_pok_6 = Image.open('images/cabeca-gengar.png')
imagem_pok_6 = imagem_pok_6.resize((40, 40))
imagem_pok_6 = ImageTk.PhotoImage(imagem_pok_6)

b_pok_6 = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=imagem_pok_6, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

### Botao 7 ###

imagem_pok_7 = Image.open('images/cabeca-dragonite.png')
imagem_pok_7 = imagem_pok_7.resize((40, 40))
imagem_pok_7 = ImageTk.PhotoImage(imagem_pok_7)

b_pok_7 = Button(janela, command=lambda: trocar_pokemon('Dragonite'), image=imagem_pok_7, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_7.place(x=375, y=340)

### Botao 8 ###

imagem_pok_8 = Image.open('images/cabeca-charizard.png')
imagem_pok_8 = imagem_pok_8.resize((40, 40))
imagem_pok_8 = ImageTk.PhotoImage(imagem_pok_8)

b_pok_8 = Button(janela, command=lambda: trocar_pokemon('Charizard'), image=imagem_pok_8, text='Charizard', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW,  padx=5, font=('Arial 12'), bg=co1, fg=co0)
b_pok_8.place(x=375, y=395)



import random
Lista_pokemons = ['Gengar', 'JigglyPuff', 'Gyarados', 'Charmander', 'Bulbasaur', 'Pikachu', 'Charizard']
pokemon_escolhido = random.sample(Lista_pokemons, 1)


trocar_pokemon(pokemon_escolhido[0])

janela.mainloop()
