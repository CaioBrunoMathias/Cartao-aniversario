from PIL import Image, ImageDraw, ImageFont
lista = ['Helder Barbalho','Daniela Barbalho','Luiziel Guedes',
         'Iran Lima','Ricardo Sefer','Hana Ghassan', 'René Souza','Ualame Machado',
         'Rômulo Rodovalho', 'Fátima Braga', 'Úrsula Vidal','Adler Silveira',
         'Nivan Noronha','José Francisco','Vera Oliveira','André Dias','José Fernando Gomes',
         'Carlos Maneschy','Ruy Cabral','Giovanni Queiróz','Mauro Ó de Almeida','Inocêncio Gasparim',
         'Jarbas Vasconcelos','Ricardo Balestreri','João Chamon','Henderson Pinto','Jaime Barbosa',
         'Giovanni Queiróz','Costa Júnior','Dilson Júnior','Hayman Apolo','Walter Resende','Rubens Leão',
         'Arthur Houat','Patrícia Heitmann']


fonte = ImageFont.truetype('./Gabriola.ttf',size=38)

for e in lista:
    imagem = Image.open('convite_.jpg')

    lapis = ImageDraw.Draw(imagem)

    lapis.text((600,200), text = f'Sr(a) {e}', fill = '#875e26', font=fonte)

    imagem.save(f'./convite_{e.strip()}.png')
