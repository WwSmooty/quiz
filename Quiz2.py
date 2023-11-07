#Quiz2.py
print ('cual es mi pelicula favorita?')
print ('Elije la opcion correcta')
print ('a) el diablo viste a la moda')
print ('b) castores zombies')
print ('c) donde estan las rubias?')
print ('d) el castillo vagabundo')
text= input('>') 
def validate_true_false(text):
    text=text.lower()
if ('a) el diablo viste a la moda' in text) or ('b) castores zombies' in text) or ('c) donde estan las rubias?'in text) or ('d) el castillo vagabundo'in text):
    print('Respuesta valida')
else:
    print('Respuesta invalida')


answer='d) el castillo vagabundo'
while answer==text:
    text=text.lower()
    if validate_true_false(text):
        if 'd) el castillo vagabundo' in text:
            print ('Respuesta correcta!')
        else:
             print('Respuesta incorrecta :(')
else:
        answer='d) el castillo vagabundo'