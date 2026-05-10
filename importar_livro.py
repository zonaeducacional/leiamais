import requests
import os
import sys
import re

def importar(book_id, titulo, autor, ano, categoria):
    # URL do cache de texto puro do Project Gutenberg
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    print(f"--- Iniciando captura de: {titulo} ---")
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar o Project Gutenberg: {e}")
        return

    texto = resposta.text

    # 1. TRATAMENTO DE CAPÍTULOS
    # Procura por 'CAPÍTULO I', 'Capítulo 1', etc., e adiciona o '#' para quebra de página
    # O regex abaixo identifica a palavra Capitulo seguida de números romanos ou cardinais
    padrao_capitulo = re.compile(r'^(CAP[ÍI]TULO\s+[0-9A-Z]+.*)$', re.IGNORECASE | re.MULTILINE)
    texto = padrao_capitulo.sub(r'# \1', texto)

    # 2. LIMPEZA DE METADADOS DO GUTENBERG (Opcional, mas ajuda)
    # Tenta cortar o texto de licença que vem antes e depois da obra
    inicio_real = re.search(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", texto)
    fim_real = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", texto)
    
    if inicio_real and fim_real:
        texto = texto[inicio_real.end():fim_real.start()]

    # 3. MONTAGEM DO CABEÇALHO (FRONT MATTER) DO HUGO
    conteudo_final = f"""---
title: "{titulo}"
autor: "{autor}"
ano: "{ano}"
categoria: "{categoria}"
---

{texto.strip()}
"""

    # 4. SALVAMENTO DO ARQUIVO
    nome_arquivo = titulo.lower().replace(" ", "-").replace("á", "a").replace("ó", "o").replace("ç", "c") + ".md"
    pasta_destino = "content/livros"
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo_final)
    
    print(f"✅ Sucesso! O livro '{titulo}' agora tem centenas de páginas.")
    print(f"📍 Local: {caminho_completo}")
    print(f"🚀 Próximo passo: git add {caminho_completo} && git commit -m 'Novo livro: {titulo}' && git push")

if __name__ == "__main__":
    # Verifica se o usuário passou os 5 argumentos necessários
    if len(sys.argv) == 6:
        importar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("\nUso correto:")
        print('python3 importar_livro.py [ID] "[Título]" "[Autor]" "[Ano]" "[Categoria]"')
        print('\nExemplo:')
        print('python3 importar_livro.py 22467 "O Cortico" "Aluisio Azevedo" "1890" "Naturalismo"')