def registrar_atividade():
    print('Registrar atividade:')
    name = str(input('Nome: '))
    while True:
        date = str(input('Data(dd/mm/aaaa): ')).split('/')
        if int(date[0]) > 31 or int(date[0]) < 1:
            print('Erro! Por favor digite um dia válido')
        print(date)
#Main program
print('Bem vindo ao sistema de gestão de projetos')
while True:
    choice = str(input('Menu:\n[1]Registrar uma nova atividade\n[2]Realizar uma análise do progresso\n'))
    match choice:
        case '1':
            registrar_atividade()