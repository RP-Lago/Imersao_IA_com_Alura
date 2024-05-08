import pandas as pd
import json

# Ler o arquivo CSV
df = pd.read_csv(r'desafios/historico_navegacao_web.csv')

# Converter a coluna 'DateTime' para datetime
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extrair a data e a hora separadamente
df['date'] = df['DateTime'].dt.date
df['time'] = df['DateTime'].dt.time

# Converter a coluna 'NavigatedToUrl' para minúsculas
df['site'] = df['NavigatedToUrl'].str.lower()

# Categorizar os sites
def classify_site(site):
    site_dict = {
        'facebook': 'social_network',
        'twitter': 'social_network',
        'instagram': 'social_network',
        'reddit': 'forum',
        'cnn': 'news',
        'bbc': 'news',
        'nytimes': 'news',
        'amazon': 'shopping',
        'ebay': 'shopping',
        'walmart': 'shopping',
        'youtube': 'video_streaming',
        'netflix': 'video_streaming',
        'hulu': 'video_streaming',
        'spotify': 'music_streaming',
        'apple_music': 'music_streaming',
        'pandora': 'music_streaming',
        'gmail': 'email',
        'outlook': 'email',
        'yahoo_mail': 'email',
        'stackoverflow': 'development',
        'github': 'development',
        'bitbucket': 'development',
        'wikipedia': 'reference',
        'google_scholar': 'reference',
        'jstor': 'reference',
        'project_euler': 'problem_solving'
    }
    for key, value in site_dict.items():
        if key in site:
            return value
    return 'other'

df['site_type'] = df['site'].apply(classify_site)

# Agrupar os sites por categoria
site_categories = {}
for category, sites in df.groupby('site_type')['site']:
    site_categories[category] = sites.tolist()

# Escrever o dicionário em um arquivo JSON
with open('site_categories.json', 'w') as f:
    json.dump(site_categories, f, indent=4)

print("Arquivo JSON criado com sucesso.")
