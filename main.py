from tkinter import *
from tkinter import ttk

from PIL import Imege, ImegeTk

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
quadro_pokemon = Frame(janela, width= 500, height=290, relief='flat')
quadro_pokemon.grid(row=1, column=0)


### nome ####
pok_nome = Label(quadro_pokemon, text='Jigglipuff', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

### Categoria ###
pok_tipo = Label(quadro_pokemon, text='Balão', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

### Identificação ###
pok_identificação = Label(quadro_pokemon, text='#039', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_identificação.place(x=12, y=75)

### imagem do Pokemon ###
imagem_pokemon = Image.open('imagens pokedex/jigglypuff.jpg')
imagem_pokemon = imagem_pokemon.resize((238, 238))
imagem_pokemon = ImageTk.PhotoImege(imagem_pokemon)

pok_imegem = Label(quadro_pokemon, image=imagem_pokemon, relief='flat',  bg=co1, fg=co0)
pok_imegem.place(x=12, y=75)

janela.mainloop()




