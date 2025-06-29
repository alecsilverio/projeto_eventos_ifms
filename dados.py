eventos = [
    {
        'nome': 'Palestra - Segurança Cibernética',
        'data': '20/05/2025',
        'tema': 'Segurança Cibernética',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3]
    },
    
    {
        'nome': 'Recepção de Calouros',
        'data': '25/05/2025',
        'tema': 'Boas-vindas aos Novos Alunos',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,]
    },
 
    {   
        'nome': 'Semana do TADS',
        'data': '10/06/2025',
        'tema': 'Tecnologia e Inovação',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,]
     }
]
participantes = {
    1: {'nome': 'Álec Silvério', 'email': 'alec@email.com', 'preferencias': ['cybersegurança', 'tecnologia']},
    2: {'nome': 'Beatriz Oliveira', 'email': 'beatriz@email.com', 'preferencias': ['inovação', 'boas-vindas']},
    3: {'nome': 'Carlos Silva', 'email': 'carlos@email.com', 'preferencias': ['tecnologia', 'cybersegurança']}
    
}

# para adicionar novos participantes

proximo_id = 4
novo_participante = {
    'nome': 'Lucas Pereira',
    'email': 'lucas@gmail.com',
    'preferencias': ['inovação', 'boas-vindas']
}

participantes[proximo_id] = novo_participante
eventos[0]['participantes'].append(proximo_id)
proximo_id += 1 # Atualiza o ID para o próximo participante

# listando os participantes em cada evento

for evento in eventos:
    print(f"Evento: {evento['nome']}")
    print(f"Data: {evento['data']}")
    print(f"Tema: {evento['tema']}")
    print(f"Local: {evento['local']}")
    print(f"Participantes: {', '.join([participantes[id]['nome'] for id in evento['participantes']])}")
    print("-" * 40) 
    
    
    