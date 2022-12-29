menu = '''
    [d] depositar
    [s] saque
    [e] extrato
    [q] sair

=> '''

saldo = 0;
limite = 500;
extrato = "";
num_saques = 0;
LIMITE_SAQUES = 3;

while True:

    op = input(menu);

    if (op == 'd'):
        valor = float(input('Informe o valor do depósito: '));
        if valor > 0:
            saldo += valor;
            extrato += f"Depósito no valor de R${valor:.2f} \n";
        else: 
            print('Não é possível realizar um depósito de valor negativo, por favor, tente novamente!');

    elif (op == 's'):
        if (num_saques < LIMITE_SAQUES):
            valSaq = float(input('Informe o valor do saque: '));
            if valSaq > saldo:
                print('Saldo insuficiente!');
            else:
                if (valSaq < 500):
                    saldo -= valSaq; 
                    extrato += f"Saque no valor de R${valSaq:.2f} \n";
                    num_saques += 1;
                else: 
                    print('O valor desejado é maior do que o permitido, por favor tente novamente.');
        else: 
            print('Você atingiu o limite de saques por hoje. Tente novamente amanhã.');
        
    elif (op == 'e'):
        print('---'*20);
        print('Não foram realizadas movimentações!' if not extrato else extrato);
        print(f'Saldo da conta: R${saldo:.2f}');
        print('---'*20);
    elif (op == 'q'):
        break;
    
    else:
        print('Operação digita inválida! Por favor, digite uma opção válida: ');