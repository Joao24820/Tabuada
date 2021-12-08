print('TABUADA DE 01 A 10 ')
num = int(input('Digite um numero para ver a tabuada: '))
sin = str(input('[+]Soma\n[-]Subtração\n[*]Multiplicação\n[/]Divisão \nInforme o sinal escolhido:'))
if sin == 'Multiplicação' or 'multiplicaçao' or 'multiplicação' or 'Multiplicaçao':
    print('{} x {} = {} '.format(num, 1, num*1))
    print('{} x {} = {} '.format(num, 2, num*2))
    print('{} x {} = {} '.format(num, 3, num*3))
    print('{} x {} = {} '.format(num, 4, num*4))
    print('{} x {} = {} '.format(num, 5, num*5))
    print('{} x {} = {} '.format(num, 6, num*6))
    print('{} x {} = {} '.format(num, 7, num*7))
    print('{} x {} = {} '.format(num, 8, num*8))
    print('{} x {} = {} '.format(num, 9, num*9))
    print('{} x {} = {} '.format(num, 10, num*10))

elif sin == 'Soma' or 'soma':
    print('{} + {} = {} '.format(num, 1, num + 1))
    print('{} + {} = {} '.format(num, 2, num + 2))
    print('{} + {} = {} '.format(num, 3, num + 3))
    print('{} + {} = {} '.format(num, 4, num + 4))
    print('{} + {} = {} '.format(num, 5, num + 5))
    print('{} + {} = {} '.format(num, 6, num + 6))
    print('{} + {} = {} '.format(num, 7, num + 7))
    print('{} + {} = {} '.format(num, 8, num + 8))
    print('{} + {} = {} '.format(num, 9, num + 9))
    print('{} + {} = {} '.format(num, 10, num + 10))

elif sin == 'Subtração' or 'subtração' or 'subtraçao' or 'Subtraçao':
    print('{} - {} = {} '.format(num, 1, num - 1))
    print('{} - {} = {} '.format(num, 2, num - 2))
    print('{} - {} = {} '.format(num, 3, num - 3))
    print('{} - {} = {} '.format(num, 4, num - 4))
    print('{} - {} = {} '.format(num, 5, num - 5))
    print('{} - {} = {} '.format(num, 6, num - 6))
    print('{} - {} = {} '.format(num, 7, num - 7))
    print('{} - {} = {} '.format(num, 8, num - 8))
    print('{} - {} = {} '.format(num, 9, num - 9))
    print('{} - {} = {} '.format(num, 10, num - 10))


elif sin =='Divisão' or 'divisão' or 'Divisao' or 'divisao':
    print('{} / {} = {} '.format(num, 1, num / 1))
    print('{} / {} = {} '.format(num, 2, num / 2))
    print('{} / {} = {:.2f} '.format(num, 3, num / 3))
    print('{} / {} = {} '.format(num, 4, num / 4))
    print('{} / {} = {} '.format(num, 5, num / 5))
    print('{} / {} = {:.2f} '.format(num, 6, num / 6))
    print('{} / {} = {:.2f} '.format(num, 7, num / 7))
    print('{} / {} = {} '.format(num, 8, num / 8))
    print('{} / {} = {:.2f} '.format(num, 9, num / 9))
    print('{} / {} = {} '.format(num, 10, num / 10))


else:
    print('Opção invalida!!')
