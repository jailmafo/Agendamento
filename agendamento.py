def adicionar_agendamento(agendamentos, data, carga):
    agendamentos.setdefault(data, []).append(carga)

def mostrar_agendamentos(agendamentos, data):
    agendamentos_para_data = agendamentos.get(data)
    if agendamentos_para_data:
        print("Agendamentos para", data, ":")
        for carga in agendamentos_para_data:
            print("-", carga)
    else:
        print("Não há agendamentos para", data)

def main():
    agendamentos = {}

    while True:
        print("\n1. Adicionar agendamento")
        print("2. Mostrar agendamentos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            data = input("Digite a data do agendamento (DD/MM/AAAA): ")
            carga = input("Digite a carga a ser agendada: ")
            adicionar_agendamento(agendamentos, data, carga)
            print("Agendamento adicionado com sucesso!")
        elif escolha == '2':
            data = input("Digite a data para mostrar os agendamentos (DD/MM/AAAA): ")
            mostrar_agendamentos(agendamentos, data)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

