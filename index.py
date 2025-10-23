from classes import GerenciadorDeAtendimentos

def main():
    gerenciador = GerenciadorDeAtendimentos()

    while True:
        print('''\nBem vindo ao sistema de atendimentos!
Selecione uma opção:
1- Adicionar atendimento
2- Pesquisar atendimentos
3- Editar atendimento
4- Remover atendimento
5- Listar atendimentos
6- Sair
''')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            nome = input("Nome do cliente: ")
            servico = input("Serviço realizado: ")
            valor = float(input("Valor do atendimento: "))
            gerenciador.adicionar_atendimento(nome, servico, valor)
            print("Atendimento adicionado com sucesso!")
        elif opcao == '2':
            termo = input("Digite o nome ou serviço para pesquisar: ")
            encontrados = gerenciador.pesquisar_atendimentos(termo)
            if encontrados:
                for a in encontrados:
                    print(a)
            else:
                print("Nenhum atendimento encontrado.")
        elif opcao == '3':
            try:
                id_editar = int(input("Digite o ID do atendimento que deseja editar: "))
                atendimento = gerenciador.buscar_por_id(id_editar)
                if atendimento:
                    print(atendimento)
                    print("O que deseja editar?")
                    print("1 - Nome")
                    print("2 - Serviço")
                    print("3 - Valor")
                    escolha = input("Escolha uma opção: ")
                    if escolha == "1":
                        novo_nome = input("Novo nome: ")
                        gerenciador.editar_atendimento(id_editar, nome=novo_nome)
                    elif escolha == "2":
                        novo_servico = input("Novo serviço: ")
                        gerenciador.editar_atendimento(id_editar, servico=novo_servico)
                    elif escolha == "3":
                        novo_valor = float(input("Novo valor: "))
                        gerenciador.editar_atendimento(id_editar, valor=novo_valor)
                    else:
                        print("Opção inválida.")
                else:
                    print("Atendimento não encontrado.")
            except ValueError:
                print("ID inválido.")
        elif opcao == '4':
            try:
                id_remover = int(input("Digite o ID do atendimento que deseja remover: "))
                gerenciador.remover_atendimento(id_remover)
                print("Atendimento removido com sucesso!")
            except (ValueError, KeyError):
                print("ID inválido ou atendimento não encontrado.")
        elif opcao == '5':
            for a in gerenciador.listar_atendimentos():
                print(a)
        elif opcao == '6':
            print("Saindo do sistema.")
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()