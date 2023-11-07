#Quiz2.py
print ('cual es mi pelicula favorita?')
print ('[Falso/Verdadero]')
text= input('>') 
def validate_true_false(text):
    text=text.lower()
if ('falso' in text) or ('verdadero' in text):
    print('Respuesta valida')
else:
    print('Respuesta invalida')

print('Cual es mi pelicula favorita?')
print ('[Falso/Verdadero]')
answer=False
while not answer:
    text= input('>') 
    text=text.lower()
    if validate_true_false(text):
        if 'verdadero' in text:
            print ('Respuesta correcta!')
        else:
             print('Respuesta incorrecta :(')
    else:
        answer=False
