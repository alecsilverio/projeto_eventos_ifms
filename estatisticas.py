
# função mostrar estatísticas 
from collections import Counter
from dados import eventos, participantes

def mostrar_estatisticas():
    print("==== Estatísticas dos Eventos ====\n")
    
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

# função para calcular a média de participação por tema
from dados import eventos
def calcular_media_participantes_por_tema():
    print("==== Média de Participação por Tema ====\n")
    total_participantes = {}  # dicionário: tema -> soma de participantes
    total_eventos = {}        # dicionário: tema -> número de eventos

    for evento in eventos:
        tema = evento['tema']
        qtd_participantes = len(evento['participantes'])

        if tema in total_participantes:
            total_participantes[tema] += qtd_participantes
            total_eventos[tema] += 1
        else:
            total_participantes[tema] = qtd_participantes
            total_eventos[tema] = 1

    for tema in total_participantes:
        media = total_participantes[tema] / total_eventos[tema]
        print(f"Tema: {tema} - Média de participantes: {media:.2f}")

#------------------------------------------------------------------

# função para contar quantos temas cada evento possui
from dados import eventos
def contar_eventos_por_tema():
    print("==== Quantidade de Eventos por Tema ====\n")
    contagem_temas = {}
    
    for evento in eventos:
        tema =  evento['tema'] 
        if tema in contagem_temas:
            contagem_temas[tema] += 1
        else:
            contagem_temas[tema] = 1
    
    for tema, quantidade in contagem_temas.items():
        print(f"Tema: {tema} - {quantidade} eventos(s).")   

#------------------------------------------------------------------

# função para possível cancelamento de eventos se não houver mais de 2 participantes
from dados import eventos 
def indentificar_eventos_para_cancelamento():
    print("\n==== Eventos com menos de 2 participantes ====\n")
    cancelaveis = [evento for evento in eventos if len(evento['participantes']) < 2]

    if cancelaveis:
        print("Eventos com baixa participação:")
    
        for evento in cancelaveis:
            print(f" - {evento['nome']} em {evento['data']} ({evento['tema']})")
    else:
        print("Todos os eventos têm 2 ou mais participantes.")
        
#------------------------------------------------------------------
