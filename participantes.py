
# Buscar participante por código
from dados import participantes, eventos

def buscar_participantes_por_codigo():
    try:
        codigo = int(input("\nDigite o ID do participante: "))
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
    
#------------------------------------------------------------------

# funçao para cadastrar novo participante
from dados import eventos, participantes
def cadastrar_novo_participante():
    global participantes 
    
    nome = input("Digite o nome do participante:")
    email = input("Digite o email do participante:")
    preferencias = input("Digite os temas de preferências do partipante: ").split(',')
    
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

#------------------------------------------------------------------

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
    
    print("Dados atuais:\n")
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

#------------------------------------------------------------------

# função para atualizar email dos participantes
from dados import participantes     
def atualizar_email_participante():
    print("\n==== Atualizar E-mail de Participante ====")
    try:
        codigo = int(input("Digite o ID do participante: "))
        if codigo not in participantes:
            print("Participante não ncontrado. ")
            return
        
        print(f"Nome: {participantes[codigo]['nome']}")
        novo_email = input("Digite o novo e-mail: ").strip()
        participantes[codigo]['email'] = novo_email
        print("E-mail.atualizado co sucesso.") 
    except ValueError:
        print("ID inválido. Digite um número. ")
        
#------------------------------------------------------------------

#função para remover participantes
from dados import participantes, eventos 
def remover_participante():
    print("==== Remover Participante ====/n")
    try:
        codigo = int(input("Digite o ID do participante que deseja remover:"))
        if codigo not in participantes:
            print("Participante não encontrado.")
            return

        nome = participantes[codigo]['nome']
        confirmacao= input(f"Tem certeza que deseja remover {nome}?  (s/n): ").lower()
        if confirmacao == 's':

            # Remover participante dos eventos
            for evento in eventos:
                if codigo in evento['participantes']:
                    evento['participantes'].remove(codigo)

            # Remover participante do dicionário
            del participantes[codigo]
            print(f"Participante '{nome}' removido com sucesso!")

        else:
            print("Remoção cancelada.")
    
    except ValueError:
        print("ID inválido. Digite um número inteiro.")

#------------------------------------------------------------------

# função para listar eventos por participante
from dados import eventos, participantes 
def listar_eventos_por_participante():
    try:
        codigo = int(input("Digite o ID do participante: "))
    except ValueError:
        print("ID inválido. Insira um número inteiro. ")
        return
    if codigo not in participantes:
        print("Participante não encontrado. ")
        return
    
    participante = participantes[codigo]
    print(f"\nEventos em que {participante['nome']} está inscrito: ")
    
    eventos_inscritos = [evento['nome'] for evento in eventos if codigo in evento['participantes']]

    if eventos_inscritos:
        for evento_nome in eventos_inscritos:
            print(f" - {evento_nome}")
    
    else: print("Este participante não está inscrito em nenhum evento.")

#------------------------------------------------------------------

# função para verificar se a participantes duplicados 
from dados import eventos 
def remover_participantes_duplicados(silencioso = False):
    total_corrigidos = 0

    for evento in eventos:
        participantes_originais = evento['participantes']
        participantes_unicos = []
        
        for id_participante in participantes_originais:
            
            if id_participante not in participantes_unicos:
                participantes_unicos.append(id_participante)
                
        if len(participantes_originais) != len(participantes_unicos):
            evento['participantes'] = participantes_unicos
            total_corrigidos += 1
            if not silencioso:
                print(f"- Duplicados removidos do evento: {evento['nome']}")

    if not silencioso:
        if total_corrigidos == 0:
            print("Nenhum evento com participantes duplicados encontrado.")
        else:
            print(f"{total_corrigidos} evento(s) corrigidos com sucesso.")
    
#------------------------------------------------------------------
