
grupos_musicales = [
    {
        'Nombre': 'BTS', 
        'Canciones': 
            [
            'Dinamite',
            'Butter',
            'Fake'
            ],
        'Mienbros': 7
    },
    {
        'Nombre': 'Blackpink', 
        'Canciones': 
            [
            'Kill this love',
            'Savage',
            'How you like that'
            ],
        'Mienbros': 4
    },
    {
        'Nombre': 'Itzy', 
        'Canciones': 
            [
            'Wannabe',
            'In the mafia',
            'No shy'
            ],
        'Mienbros': 5
    }
]

name_group = 'Blackpink'

result = list(filter(lambda grupo: grupo['Nombre'] == name_group, grupos_musicales))
print(result)

