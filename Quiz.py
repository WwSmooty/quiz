#Simple quiz
print ('El sol y la luna tienen el mismo radio aparentemente?')
print ('[Falso/Verdadero]')
text= input('>') 

def validate_true_false(text):
    text=text.lower()
if ('falso' in text) or ('verdadero' in text):
    print('Respuesta valida')
else:
    print('Respuesta invalida')

print ('El sol y la luna tienen el mismo radio aparente durante un eclipse de sol?')
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
