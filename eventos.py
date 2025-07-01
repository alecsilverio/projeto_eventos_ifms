
# Função para listar eventos e seus participantes
from dados import eventos, participantes

def listar_eventos_participantes():
    for evento in eventos:
        print(f"\nEvento: {evento['nome']} - {evento['tema']}")
        print(f"Data: {evento['data']}")
        print(f"Tema: {evento['tema']}")
        print(f"Local: {evento['local']}")
        nomes = ", ".join([participantes[id]['nome'] for id in evento['participantes']])
        print(f"Participantes: {nomes}")
        print("-" * 40)
        
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

# função para remover eventos
from dados import eventos
def remover_evento():
    print("==== Remover Evento ====/n")
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

# funções para atualizar tema de um evento e atualizar email dos participantes 
from dados import eventos     
def atualizar_tema_evento():
    print("\n==== Atualizar Tema de Evento ====\n")
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

#------------------------------------------------------------------

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
    
    print("==== Eventos Agrupados por tema ====\n")
    for tema, lista_eventos in temas.items():
        print(f"\nTema: {tema}")
        for nome in lista_eventos:
            print(f" - {nome}")
            
#------------------------------------------------------------------




