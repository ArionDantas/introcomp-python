#algoritimo para descobrir o seu IMC (indice de massa corporal)

peso = float(input('qual o seu peso: '))
altura = float(input('qual a sua altura: '))

descobrirImc = peso / (altura ** 2)
print('O seu IMC é {:.1f}' .format(descobrirImc))
if descobrirImc < 18.5:
    print('você está abaixo do peso')
elif descobrirImc >= 18.5 and descobrirImc < 25 :
    print('você está saudável')
elif descobrirImc >= 25 and descobrirImc < 30:
    print('Peso em excesso')
elif descobrirImc >= 30 and descobrirImc < 35 :
    print('Obesidade grau I')
elif descobrirImc >= 35 and descobrirImc < 40 :
    print('Obesidade grau II')
elif descobrirImc >= 40:
    print('Obesidade grau III')
    