# Imersão Inteligência Artificial 2ª Edição

# Usando o código Python para transcrever imagens em texto com a API do Google
**Requisitos:**
Python 3.7 ou superior
Bibliotecas pathlib, hashlib e google-generativeai
Chave de API do Google Generative AI
Passos:
Configurando a API:
Substitua "YOUR_API_KEY" pela sua chave de API do Google Generative AI.
Ajustando configurações:
generation_config: Define parâmetros como temperatura e comprimento máximo do texto gerado.
safety_settings: Configura filtros de segurança para evitar conteúdo prejudicial.
Preparando as imagens:
A função upload_if_needed carrega as imagens para a API e as adiciona ao prompt.
Substitua "Cole o caminha da sua imagem" pelo caminho da sua imagem (pode adicionar até 3 imagens).
Gerando o texto:
O modelo Gemini processa as imagens e gera o texto descritivo.
O resultado é impresso na tela.
Limpeza:
As imagens carregadas são apagadas do servidor após o uso.
Observações:
O modelo Gemini está em desenvolvimento e pode ter limitações.
A qualidade da transcrição depende da qualidade da imagem e do conteúdo.
É importante revisar o texto gerado e fazer ajustes se necessário.
Exemplo de uso:
# Caminhos das imagens
imagem1 = "imagens/gato.jpg"
imagem2 = "imagens/cachorro.png"

# Ajustando o prompt
prompt_parts = [
    "que é essa imagem ",
    *upload_if_needed(imagem1),
    *upload_if_needed(imagem2),
    " ",
]

# Gerando o texto
response = model.generate_content(prompt_parts)
print(response.text)

