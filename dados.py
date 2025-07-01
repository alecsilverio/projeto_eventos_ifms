
eventos = [
    {
        'nome': 'Palestra - Segurança Cibernética',
        'data': '02/02/2025',
        'tema': 'Segurança Cibernética',
        'local': 'Auditório do Ifms',
        'participantes': [2,2,3,4]
    },
    
    {
        'nome': 'Recepção de Calouros',
        'data': '25/05/2025',
        'tema': 'Boas-vindas aos Novos Alunos',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,]
    },
     {
        'nome': 'IF Arraiá',
        'data': '16/06/2025',
        'tema': 'Festa Junina',
        'local': 'Pátio do IFMS',
        'participantes': [1]
    },

    {   
        'nome': 'Semana do TADS',
        'data': '10/06/2025',
        'tema': 'Tecnologia e Inovação',
        'local': 'Auditório do Ifms',
        'participantes': [1,2,3,4]
    }
]
participantes = {
    1: {'nome': 'Álec Silvério', 'email': 'alec@email.com', 'preferencias': ['cybersegurança', 'tecnologia']},
    2: {'nome': 'Beatriz Oliveira', 'email': 'beatriz@email.com', 'preferencias': ['inovação', 'boas-vindas']},
    3: {'nome': 'Carlos Silva', 'email': 'carlos@email.com', 'preferencias': ['tecnologia', 'cybersegurança']},
    4: {'nome': 'Mariana Nogueira', 'email': 'mariana10@email.com', 'preferencias': ['engenharias', 'cybersegurança']},
    
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


    
    
    