import subprocess

while True:
    comando = input('comando: ')
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        saida = resultado.stdout

        if saida is not None:
            print(saida)
        else:
            print('\033[1;32mComando executado com sucesso.\033[m')
        print()

    except subprocess.CalledProcessError as e:
        print(e)
        print()
