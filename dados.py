
eventos = [
    {
        'nome': 'Palestra - Segurança Cibernética',
        'data': '02/02/2025',
        'tema': 'Segurança Cibernética',
        'local': 'Auditório do Ifms',
        'participantes': [2,2,3,4],
        'carga_horaria': 3,
        'organizador': 'Coordenação e Centro Acadêmico',
    },
    
    {
        'nome': 'Recepção de Calouros',
        'data': '25/05/2025',
        'tema': 'Boas-vindas aos Novos Alunos',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,],
        'carga_horaria': 1,
        'organizador': 'Centro Acadêmico',
    },
     {
        'nome': 'IF Arraiá',
        'data': '16/06/2025',
        'tema': 'Festa Junina',
        'local': 'Pátio do IFMS',
        'participantes': [1],
        'carga_horaria': 2,
        'organizador': 'Centro Acadêmico',
    },

    {   
        'nome': 'Semana do TADS',
        'data': '10/06/2025',
        'tema': 'Tecnologia e Inovação',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,4],
        'carga_horaria': 5,
        'organizador': 'Coordenação e Centro Acadêmico',
    }
]
participantes = {
    1: {'nome': 'Álec Silvério', 'email': 'alec123@email.com', 'preferencias': ['cybersegurança', 'tecnologia']},
    2: {'nome': 'Beatriz Oliveira', 'email': 'beatriz89@email.com', 'preferencias': ['inovação', 'boas-vindas']},
    3: {'nome': 'Carlos Silva', 'email': 'carlos20@email.com', 'preferencias': ['tecnologia', 'cybersegurança']},
    4: {'nome': 'Mariana Nogueira', 'email': 'mariana10@email.com', 'preferencias': ['engenharias', 'boas-vindas']},
    5: {'nome': 'Miguel Tavares', 'email': 'tavares15@email.com', 'preferencias': ['engenharias', 'Inteligência Artificial']},
    
}

# para adicionar novos participantes
proximo_id = 6
novo_participante = {
    'nome': 'Lucas Pereira',
    'email': 'lucas@gmail.com',
    'preferencias': ['inovação', 'boas-vindas']
}

participantes[proximo_id] = novo_participante
eventos[0]['participantes'].append(proximo_id)
proximo_id += 1 # Atualiza o ID para o próximo participante


    
    
    