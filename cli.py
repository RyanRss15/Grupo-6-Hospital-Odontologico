import agendamento

def cli():
    cmd = ""
    print("=== Bem-vindo ao sistema de agendamento automático ===")

    while True:
        print("\nInsira o Login e a Senha para continuar.")
        login = input("Login: ")
        senha = input("Senha: ")
        
        if login and senha:
            break
        print("Erro: Login e Senha são obrigatórios.")

    id_agenda = int(input("Insira o ID da agenda (calendário): ")) #280
    n_pacientes = int(input("Insira quantos pacientes deseja agendar: "))
    n_dias = int(input("Insira quantos dias a partir de hoje deseja preencher: "))

    print("\nLendo planilha e processando agendamentos...")
    
    try:
        agendamento.agendamento(login, senha, n_pacientes, n_dias + 1, id_agenda)
        print("\nProcesso finalizado com sucesso!")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante o processamento: {e}")
    while cmd.upper() != "X":
        cmd = input("Insira 'X' para sair: ")