from math import sin , cos , tan , radians
ang = int(input('Digite um angulo qualquer:'))
angulo = radians(ang)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print(f'VALORES :\n SENO : {seno:.2f}\n COSSENO : {cosseno:.2f} \n TANGENTE : {tangente:.2f}')
