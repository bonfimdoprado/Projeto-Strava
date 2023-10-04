import pandas as pd

analise_strava = pd.read_excel('banco_strava_completo.xlsx')
strava_gxp = analise_strava[analise_strava['Cidade'] == 'Guaxupé']


# Solicitar entrada do usuário para os novos dados
nova_distancia = float(input("Digite a nova distância: "))
nova_elevacao = float(input("Digite a nova elevação: "))
novo_tempo_movimentacao = float(input("Digite o novo tempo de movimentação: "))

# Criar um DataFrame com as previsões para a nova atividade
nova_atividade = pd.DataFrame({
    'Elevacao (m)': [nova_elevacao],
    'Distancia (km)': [nova_distancia],
    'Tempo de movimentação': [novo_tempo_movimentacao]
})

# Margens
margem = 10
margem1 = 150
margem2 = 30
margem_distancia = (nova_distancia - margem, nova_distancia + margem)
margem_elevacao = (nova_elevacao - margem1, nova_elevacao + margem1)
margem_tempo = (novo_tempo_movimentacao - margem2, novo_tempo_movimentacao + margem2)

# Filtrar atividades dentro das margens e que não contenham as palavras "Pedalada" e "Cycling"
atividades_recomendadas = strava_gxp[
    (strava_gxp['Distancia (km)'] >= margem_distancia[0]) & (strava_gxp['Distancia (km)'] <= margem_distancia[1]) &
    (strava_gxp['Elevacao (m)'] >= margem_elevacao[0]) & (strava_gxp['Elevacao (m)'] <= margem_elevacao[1]) &
    (strava_gxp['Tempo de movimentação'] >= margem_tempo[0]) & (strava_gxp['Tempo de movimentação'] <= margem_tempo[1]) &
    (~strava_gxp['Atividade'].str.contains('Pedalada|Cycling|Passeio|Ride', case=False, regex=True))
]

# Ordenar atividades por previsão de velocidade média
atividades_recomendadas = atividades_recomendadas.sort_values(by='Veloc Media (km/h)', ascending=False)

# Limitar a até 3 atividades recomendadas
atividades_recomendadas = atividades_recomendadas.head(3)

# Apresentar a recomendação ao usuário
#print("Atividades Recomendadas:")
#print(atividades_recomendadas[['Atividade', 'Data', 'Distancia (km)',
                               'Tempo de movimentação', 'Elevacao (m)', 'Veloc Media (km/h)']])
