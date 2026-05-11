import requests
import os
import sys
import re
import unicodedata

def slugify(text):
    text = text.lower()
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

def importar(book_id, titulo, autor, ano, categoria):
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
    padrao_capitulo = re.compile(r'^(CAP[ÍI]TULO\s+[0-9A-Z]+.*)$', re.IGNORECASE | re.MULTILINE)
    texto = padrao_capitulo.sub(r'# \1', texto)

    # 2. LIMPEZA DE METADADOS DO GUTENBERG
    inicio_real = re.search(r"\*\*\* START OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", texto)
    fim_real = re.search(r"\*\*\* END OF THE PROJECT GUTENBERG EBOOK .* \*\*\*", texto)
    
    if inicio_real and fim_real:
        texto = texto[inicio_real.end():fim_real.start()]

    # 3. MONTAGEM DO CABEÇALHO (FRONT MATTER)
    # Escapar aspas duplas nos campos para não quebrar o YAML
    titulo_esc = titulo.replace('"', '\\"')
    autor_esc = autor.replace('"', '\\"')
    
    conteudo_final = f"""---
title: "{titulo_esc}"
autor: "{autor_esc}"
ano: "{ano}"
categoria: "{categoria}"
capa: ""
sinopse: "Sinopse ainda não disponível para esta obra clássica."
---

{texto.strip()}
"""

    # 4. SALVAMENTO DO ARQUIVO (Slugify garantido)
    nome_arquivo = slugify(titulo) + ".md"
    pasta_destino = "content/livros"
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo_final)
    
    print(f"✅ Sucesso! O livro '{titulo}' agora tem centenas de páginas.")
    print(f"📍 Local: {caminho_completo}")

if __name__ == "__main__":
    if len(sys.argv) == 6:
        importar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("\nUso correto: python3 importar_livro.py [ID] [Titulo] [Autor] [Ano] [Categoria]")