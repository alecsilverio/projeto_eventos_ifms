
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

#------------------------------------------------------------------

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
    
#------------------------------------------------------------------

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
    
    print("\nDados atuais:")
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
 
# função mostrar estatísticas 
from collections import Counter
from dados import eventos, participantes

def mostrar_estatisticas():
    print("\n==== Estatísticas dos Eventos ====")
    
    # participantes mais ativos
    contagem_participantes = Counter()
    for evento in eventos:
        contagem_participantes.update(evento['participantes'])
        
    mais_ativos = contagem_participantes.most_common(3)
    print("Participantes mais ativos:")
    for id_part, total in mais_ativos:
        nome = participantes[id_part]['nome']
        print(f" - {nome}: inscrito em {total} eventos(s)")
    
    print()
    
    # temas mais frequentes
    contagem_temas = Counter()
    for evento in eventos:
        contagem_temas[evento['tema']] += 1
        
    print("Temas mais frequentes:")
    for tema, total in contagem_temas.most_common():
        print(f" - {tema}: {total} evento(s)")

    print()
    
#------------------------------------------------------------------

# função para remover eventos
from dados import eventos
def remover_evento():
    print("\n==== Remover Evento ====")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento['nome']} ({evento['data']})")
    
    try: 
        escolha = int(input("Digite o número do evento que deseja remover:"))
        if 1 <= escolha <= len(eventos):
            eventos_removido = eventos.pop(escolha - 1)
        else: 
            print("Número invalido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
        
#------------------------------------------------------------------

#função para remover participantes
from dados import participantes, eventos 
def remover_participante():
    print("\n==== Remover Participante ====")
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

# função para cadastrar novo evento
from dados import eventos, participantes
def cadastrar_evento():
    print("\n==== Cadastro de Novo Evento ====")
    nome = input("Digite o nome do evento: ").strip()
    data = input("Digite a data do evento (dd/mm/aaaa): ").strip()
    tema = input("Digite o tema do evento: ").strip()
    local = input("Digite o local do evento: ").strip()
   
   #partricipantes
    ids = input("Digite os IDs dos participantes (separados por virgula): ").strip()
    lista_ids = []
    if ids:
        try:
            lista_ids = [int(id.strip()) for id in ids.split(',') if int(id.strip()) if participantes]
        except ValueError:
            print("IDs inválidos. Certifique-se de digitar números inteiros separados por vírgula.")
            lista_ids = []
    
    novo_evento = {
        'nome': nome,
        'data': data,
        'tema': tema,
        'local': local,
        'participantes': lista_ids
    }
    eventos.append(novo_evento)
    print(f"\nEvento '{nome}' cadatrado com sucesso!")

#------------------------------------------------------------------

# funções para atualizar tema de um evento e atualizar email dos participantes 
from dados import eventos     # atualizar tema de um evento 
def atualizar_tema_evento():
    print("\n==== Atualizar Tema de Evento ====")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento['nome']} (Tema atual: {evento['tema']})")
        
    try:
        escolha = int(input("Digite o número do Evento que deseja atualizar:"))
        if 1 <= escolha <= len(eventos):
            novo_tema = input("Digite o novo tema do evento: ").strip()
            eventos[escolha - 1]['tema'] = novo_tema
            print("Tema atualizado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número. ")


from dados import participantes     # atualizar email dos participantes
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

# função para verificar se a participantes duplicados 
from dados import eventos 
def remover_participantes_duplicados():
    print("\n==== Remoção de Participantes Duplicados ====")
    total_corrigidos = 0

    for evento in eventos:
        participantes_originais = evento['participantes']
        participantes_unicos = []
        for id_part in participantes_originais:
            if id_part not in participantes_unicos:
                participantes_unicos.append(id_part)
        if len(participantes_originais) != len(participantes_unicos):
            evento['participantes'] = participantes_unicos
            total_corrigidos += 1
            print(f"- Duplicados removidos do evento: {evento['nome']}")

    if total_corrigidos == 0:
        print("Nenhum evento com participantes duplicados encontrado.")
    else:
        print(f"{total_corrigidos} evento(s) corrigidos com sucesso.")
    
#------------------------------------------------------------------

# função para buscar eventos por tema
from datetime import datetime
from dados import eventos

def buscar_eventos_por_tema():
    tema_busca = input("Digite o tema que deseja buscar: ").strip().lower()
    
    encontrados = [evento for evento in eventos if tema_busca in evento['tema'].strip().lower()]

    if encontrados:
        print(f"\nEventos encontrados com tema '{tema_busca}':")
        for evento in encontrados:
            print(f"- {evento['nome']} ({evento['data']}) - {evento['tema']}")
    else:
        print("Nenhum evento encontrado com esse tema.")

# função para buscar eventos por faixa de datas
def buscar_eventos_por_faixa_de_datas():
    print("\n==== Buscar Eventos por Faixa de Datas ====")
    data_inicio_str = input("Digite a data inicial (dd/mm/aaaa): ").strip()
    data_fim_str = input("Digite a data final (dd/mm/aaaa): ").strip()

    try:
        data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y").date()
        data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y").date()
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")
        return

    eventos_encontrados = []
    for evento in eventos:
        try:
            data_evento = datetime.strptime(evento['data'].strip(), "%d/%m/%Y").date()
        except ValueError:
            print(f"Data inválida no evento: {evento['nome']}")
            continue

        if data_inicio <= data_evento <= data_fim:
            eventos_encontrados.append(evento)

    if eventos_encontrados:
        print(f"\nEventos entre {data_inicio_str} e {data_fim_str}:")
        for evento in eventos_encontrados:
            print(f"- {evento['nome']} em {evento['data']} ({evento['tema']})")
    else:
        print("Nenhum evento encontrado no intervalo informado.")

#------------------------------------------------------------------

# função para agrupar eventos por tema 
from collections import defaultdict
def agrupar_eventos_por_tema():
    from dados import eventos 
    temas = defaultdict(list)
        
    for evento in eventos:
        temas[evento['tema']].append(evento['nome'])
    
    print("\n==== Eventos Agrupados por tema ====")
    for tema, lista_eventos in temas.items():
        print(f"\nTema: {tema}")
        for nome in lista_eventos:
            print(f" - {nome}")
            
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









