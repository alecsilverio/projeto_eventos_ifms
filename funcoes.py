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
            
    
    