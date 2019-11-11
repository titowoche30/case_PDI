import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def weighted_mean_color(colors):
    #Lista com as cores.
    rgbs = [colors[i][1] for i in range(len(colors))]
    #Lista com os pesos.
    weights = [colors[i][0] for i in range(len(colors))]
    
    #Média ponderada das cores.
    weighted_avg = np.average(rgbs, weights=weights,axis=0)
    #Média ponderada das cores arredondada.
    weighted_avg = [int(round(i)) for i in weighted_avg]
    
    return weighted_avg


def get_font_size(img,font_name,name):
    #img = objeto do tipo Image.
    #font_name = nome da fonte a ser usada
    #name = string com o nome que será determinado o tamanho.

    fontsize = 1
    
    #Parte da largura da imagem
    img_fraction = 0.40
    
    font = ImageFont.truetype(font_name, fontsize)
    
    #Vai iterar enquanto o tamanho do texto for menor que o criterio
    while font.getsize(name)[0] < img_fraction*img.size[0]:
        fontsize += 1
        font = ImageFont.truetype(font_name, fontsize)
    
    fontsize -= 1
    return fontsize
    

if len(sys.argv) < 4:
    print('4 argumentos sao necessarios, {} foram fornecidos.'.format(len(sys.argv)))
    sys.exit()


##-------Trata os parâmetros------##
image,font,name,coordinates = sys.argv[1:]

coordinates= eval(coordinates)
x,y = coordinates
image_name = 'mockups/' + image + '.jpg'
font_name = 'fonts/' + font + '.ttf'

##-------Cria o objeto da imagem-------##
img = Image.open(image_name)

#-------Pega o tamanho de fonte para o texto a ser escrito-------##
font_size = get_font_size(img,font_name,name)

##-------Cria o objeto fonte-------##
fnt = ImageFont.truetype(font_name,font_size)

##-------Cria o objeto que irá escrever na imagem-------##
draw = ImageDraw.Draw(img)

##-------Pega o tamanho em pixels (x,y) da imagem-------##
img_size = img.size

##-------Pega a parte da imagem onde o texto será escrito-------##
box = (x, y, x+fnt.getsize(name)[0], y+fnt.getsize(name)[1])

##-------Cria um objeto de imagem somente com a parte onde o texto será escrito-------##
croped = img.crop(box)
croped.load()

##-------Pega as cores da parte onde o texto será escrito-------##
colors = croped.getcolors(croped.size[0]*croped.size[1])

##-------Faz uma média ponderada com as cores da parte da imagem onde o texto será escrito-------##
color = weighted_mean_color(colors)

##-------Gera a cor para o texto pegando a cor complementar-------##  
text_color = [255-color[0] , 255-color[1],255-color[2]]

##-------Escreve o texto na imagem-------##
draw.text(coordinates,name, font=fnt, fill=tuple(text_color))

##-------Salva a imagem com o texto escrito-------##
img.load()
img.save(image + '_' + name + '.jpg')
