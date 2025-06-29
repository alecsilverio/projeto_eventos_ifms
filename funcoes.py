from dados import eventos, participantes

def listar_eventos_participantes():
    for evento in eventos:
        print(f"Evento: {evento['nome']}")
        nomes = ", ".join([participantes[id]['nome'] for id in evento ['participantes']])
        print(f'"Participantes: {nomes}" ')
        print(f"-" * 40)

