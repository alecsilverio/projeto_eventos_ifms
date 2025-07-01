from dados import eventos, participantes

def gerar_certificados_participante(participante_id, *args, **kwargs):
    if participante_id not in participantes:
        print("Participante não encontrado.")
        return

    participante = participantes[participante_id]
    nome = participante['nome']
    certificados_gerados = False

    for evento in eventos:
        if participante_id in evento['participantes']:
            certificados_gerados = True
            carga = evento.get('carga_horaria', 2)
            nome_evento = evento['nome']
            data = evento['data']
            local = evento['local']
            organizador = evento.get('organizador', kwargs.get('organizador', 'Organizador Desconhecido'))

            print("="*60)
            print(f"{'CERTIFICADO DE PARTICIPAÇÃO':^60}")
            print("-"*60)
            print(f"Certificamos que {nome} participou do evento:")
            print(f"'{nome_evento}' realizado em {data}, no {local}.")
            print(f"Carga horária: {carga} horas.")
            print(f"Organizador: {organizador}")
            for extra in args:
                print(extra)
            for chave, valor in kwargs.items():
                if chave != "organizador":
                    print(f"{chave.capitalize()}: {valor}")
            print("="*60)
            print("\n")

    if not certificados_gerados:
        print("Este participante ainda não participou de nenhum evento.")