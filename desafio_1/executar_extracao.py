'''crie um pronpt que leia o CSV fornecido, que registra meus acessos à internet. A partir desses dados, realize as seguintes tarefas:
1.	Classifique os sites visitados de acordo com o nome do site.
2.	Calcule a quantidade total de acessos para cada site.
3.	Identifique em quais dias ocorreram os acessos.
4.	Classifique os sites de acordo com o seu tipo (por exemplo, redes sociais, notícias, compras, etc.).
5.	Com base nessas informações, gere um resumo dos meus padrões de acesso à internet.
6.	Finalmente, forneça algumas conclusões sobre como tenho utilizado o meu tempo na internet, com base nos padrões identificados.'''

import json
import pandas as pd

# Carregar o dicionário de classificação de sites a partir de um arquivo JSON
with open(r'RP-Lago/Imersao_IA_com_Alura/desafios/site_categories.json') as f:
    site_dict = json.load(f)

df = pd.read_csv(r'RP-Lago/Imersao_IA_com_Alura/desafios/historico_navegacao_web.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['site'] = df['NavigatedToUrl'].str.lower()

def classify_site(site):
    for key, value in site_dict.items():
        if site in value:
            return key
    return 'other'

df['site_type'] = df['site'].apply(classify_site)

# Calculando a quantidade total de acessos para cada tipo de site
grouped = df.groupby(['site_type']).size().reset_index(name='counts')

print(grouped)