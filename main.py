import api

cmd = ""
id_calendario = 280                         # Será possível selecionar entre os calendários disponíveis
data = "10/12/2025"                         # Data do agendamento. Será dinâmica
data2 = "2025-12-10"                        # Endpoints diferentes da API pedem formatos diferentes...
local = 1                                   # 1 = Geral/CONSULTÓRIO; 2 = CIn; 3 = CCM
paciente_planilha = {                       # Será resgatado automaticamente da planilha
    "nome" : "JEFERSON DE JESUS FERNANDES",
    "data_nascimento" : "14/03/1999",
    "cpf" : "07469419519"
}
data_hoje = "2025-12-09"                    # Será resgatada automaticamente pelo sistema

if __name__ == "__main__":
    #login = input("Insira o login: ")
    #password = input("Insira a senha: ")

    ti_saude_api = api.TISaudeAPI("", "") # LOGIN E SENHA AQUI

    hora_primeiro_agendamento = ti_saude_api.get_horarios(id_calendario, data2, local) # Resgata o primeiro horário disponível na data selecionada

    id_paciente, nome_paciente = ti_saude_api.get_pacientes(paciente_planilha["cpf"]) # Resgata o ID e o nome do paciente pelo CPF

    resposta_agendamento = ti_saude_api.post_agendamento(
        id_paciente,
        nome_paciente,
        data,
        local,
        id_calendario,
        hora_primeiro_agendamento
    )

    print(resposta_agendamento)

    print("Insira 'X' para sair")
    while cmd != "X":
        cmd = input("")