    # Função para listar eventos e seus participantes
from dados import eventos, participantes

def listar_eventos_participantes():
    for evento in eventos:
        print(f"Evento: {evento['nome']} - {evento['tema']}")
        print(f"Data: {evento['data']}")
        print(f"Tema: {evento['tema']}")
        print(f"Local: {evento['local']}")
        nomes = ", ".join([participantes[id]['nome'] for id in evento['participantes']])
        print(f"Participantes: {nomes}")
        print("-" * 40)

# Buscar participante por código
from dados import participantes, eventos

def buscar_participantes_por_codigo():
    try:
        codigo = int(input("Digite o ID do participante: "))
    except ValueError:
        print("ID inválido. Por favor, insira um número inteiro.")
        return
    
    if codigo not in participantes:
        print("Participantes não encontrao. ")
        return
    
    participante = participantes[codigo]
    print(f"Nome: {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print(f"Preferências: {', '.join(participante['preferencias'])}")
    
    eventos_participando = [
        evento['nome'] for evento in eventos if codigo in evento['participantes']
    ]
    
    if eventos_participando:
        print("Inscrito nos eventos:")
        for nome_evento in eventos_participando:
            print(f" - {nome_evento}")
    else: 
        print("Este participante ainda não está inscrito em nenhum evento.")
    
# funçao para cadastrar novo participante
from dados import eventos, participantes
def cadastrar_novo_participante():
    global participantes 
    
    nome = input("Digite o nome do participante:")
    email = input("Digite o email do participante:")
    preferencias = input("Digite as preferências do partipante: ").split(',')
    
    novo_id = max(participantes.keys()) + 1
    participantes[novo_id] ={
        'nome': nome.strip(),
        'email': email.strip(),
        'preferencias': [p.strip() for p in preferencias]
    }
    
    print("\nEventos disponíveis:")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento['nome']}")
    
    try:
        escolha = int(input("Escolha um evento para inscrever o participante (número):"))
        eventos[escolha - 1]['participantes'].append(novo_id)
        print(f"\nParticipante {nome} cadastrado e inscrito no evento com sucesso!\n")
    except (ValueError, IndexError):
        print("Evento inválido. Participante cadastrado, mas não está inscrito em nenhum evento.")

# função para editar dados dos participantes
from dados import participantes 
def editar_participante():
    try:
        codigo = int(input("Digite o ID do participante que deseja editar: "))
    except ValueError:
        print("ID inválido. ")
        return
    if codigo not in participantes:
        print("Participante não encontrado.")
        return
    participante = participantes[codigo]
    
    print("\Dados atuais:")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print(f"Preferências: {', '.join(participante['preferencias'])}")
    
    print("\nDigite os novos dados (aperte enter para manter o atual):")
    novo_nome = input("Novo nome:")
    novo_email = input("Novo e-mail:")
    novas_preferencias = input("Novas preferências (separadas por vírgula):")
    
    if novo_nome.strip():
        participante['nome'] = novo_nome.strip()
    if novo_email.strip():
        participante['email'] = novo_email.strip()
    if novas_preferencias.strip():
        participante['preferencias'] = [p.strip() for p in novas_preferencias.split(',')]   
    
    print("\nDados atualizados com sucesso!")
    