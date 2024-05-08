# Imersão Inteligência Artificial 2ª Edição
# Categorização de Sites Web a partir do Histórico de Navegação


**Descrição:**
Este projeto tem como objetivo categorizar sites web a partir de um histórico de navegação, utilizando a linguagem Python e as bibliotecas Pandas e Json.
#**Funcionamento**
O projeto consiste em dois scripts Python principais:
**Script 1 (trecho-1):**
**Leitura dos dados:** O script lê um arquivo CSV contendo o histórico de navegação web, com colunas como data/hora e URL visitada.
**Pré-processamento:** Converte a coluna de data/hora para o formato datetime, extrai a data e a hora em colunas separadas e converte as URLs para minúsculas.
**Categorização:** Define uma função para classificar os sites em categorias predefinidas (redes sociais, fóruns, notícias, etc.) com base em palavras-chave presentes na URL.
**Agrupamento:** Agrupa os sites por categoria e armazena os resultados em um dicionário.
**Exportação:** Salva o dicionário de categorias em um arquivo JSON para uso posterior.
**Script 2 (trecho-2):**
Carregamento dos dados: Lê o arquivo CSV do histórico de navegação e o arquivo JSON com as categorias de sites.
**Pré-processamento:** Realiza o mesmo pré-processamento do **primeiro script.**
Classificação: Utiliza a função de classificação e o dicionário de categorias para classificar cada site visitado.
Contagem: Agrupa os sites por categoria e conta o número de acessos em cada uma.
Exibição: Mostra a quantidade total de acessos para cada tipo de site.
#**Arquivos**
**historico_navegacao_web.csv:** Arquivo CSV contendo o histórico de navegação web.
**site_categories.json:** Arquivo JSON contendo o dicionário que mapeia palavras-chave a categorias de sites.
script_1.py: Script Python para categorizar e agrupar **sites (trecho-1).**
**script_2.py:** Script Python para contar o número de acessos por categoria de site (trecho-2).
#**Como usar**
Certifique-se de ter as bibliotecas Pandas e Json instaladas no seu ambiente Python.
Substitua o arquivo historico_navegacao_web.csv com seu próprio histórico de navegação.
Adapte o dicionário de categorias em site_categories.json ou no script 1, se necessário.
Execute o script 1 para gerar o arquivo JSON com as categorias.
Execute o script 2 para analisar o histórico de navegação e exibir a quantidade de acessos por categoria.
Possíveis Aplicações
Análise de hábitos de navegação: Entender como o tempo é gasto online.
**Controle parental:** Monitorar o tipo de conteúdo acessado por crianças.
Recomendação de sites: Sugerir sites similares com base no histórico de navegação.
Bloqueio de sites: Bloquear o acesso a determinadas categorias de sites.

