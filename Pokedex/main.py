from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.tix import TEXT

#importando Pillow
from PIL import Image, ImageTk

# cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#criação da janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


#nome
pok_nome = Label(frame_pokemon, text='Pikachu', relief= 'flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

#categoria
pok_tipo = Label(frame_pokemon, text='Eletrico', relief= 'flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

#id
pok_id = Label(frame_pokemon, text='#025', relief= 'flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# Imagem do Pokemon
imagem_pokemon = Image.open('images/pikachu.png')
imagem_pokemon = imagem_pokemon.resize((238, 238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief= 'flat', bg=co1, fg=co0)
pok_imagem.place(x=60, y=50)

pok_tipo.lift()

# Status
pok_status = Label(janela, text='Status', relief= 'flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

#Vida
pok_hp = Label(janela, text='HP: 100', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

#Ataque
pok_atack = Label(janela, text='Ataque: 600', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15, y=385)

#Defesa
pok_defesa = Label(janela, text='Defesa: 100', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

#Velocidade
pok_velocidade = Label(janela, text='Velocidade: 100', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

#Total
pok_total = Label(janela, text='Total: 100', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# Habilidades
pok_habilidade = Label(janela, text='Habilidades', relief= 'flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidade.place(x=180, y=310)

#Vida
pok_hb1 = Label(janela, text='Jato de Agua', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195, y=360)

#Ataque
pok_hb2 = Label(janela, text='Soco Eletrico', relief= 'flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195, y=385)


# Criando Botoes para Pokemon

#Imagem Pokemon 1 Pikachu
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1 = Button(janela, image=imagem_pokemon_1, text='Pikachu', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

#Imagem Pokemon 2 Bulbasaur
imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_1 = Button(janela, image=imagem_pokemon_2, text='Bulbasaur', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=65)

#Imagem Pokemon 3 Charmander
imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_1 = Button(janela, image=imagem_pokemon_3, text='Charmander', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=120)

#Imagem Pokemon 4 Gyarados
imagem_pokemon_4 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_1 = Button(janela, image=imagem_pokemon_4, text='Gyarados', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=175)

#Imagem Pokemon 5 Gengar
imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_1 = Button(janela, image=imagem_pokemon_5, text='Gengar', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=230)

#Imagem Pokemon 6 Dragonoide
imagem_pokemon_6 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_1 = Button(janela, image=imagem_pokemon_6, text='Dragonite', width=150, relief= 'raised', overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=285)




janela.mainloop()