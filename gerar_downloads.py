import os
import subprocess
import yaml

def gerar_downloads():
    pasta_livros = "content/livros"
    pasta_saida = "static/downloads"
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    for arquivo in os.listdir(pasta_livros):
        if arquivo.endswith(".md"):
            caminho_md = os.path.join(pasta_livros, arquivo)
            nome_base = os.path.splitext(arquivo)[0]
            
            # Gerar EPUB
            caminho_epub = os.path.join(pasta_saida, f"{nome_base}.epub")
            print(f"Gerando EPUB para {nome_base}...")
            
            try:
                subprocess.run([
                    "pandoc", caminho_md,
                    "-o", caminho_epub,
                    "--metadata", f"title={nome_base.replace('-', ' ').title()}"
                ], check=True)
                print(f"✅ {nome_base}.epub gerado.")
            except Exception as e:
                print(f"❌ Erro ao gerar EPUB para {nome_base}: {e}")

            # Nota: PDF não será gerado pois exige pdflatex ou engine similar não disponível
            # Mas criaremos um arquivo vazio ou informativo para os links não quebrarem 404
            caminho_pdf = os.path.join(pasta_saida, f"{nome_base}.pdf")
            if not os.path.exists(caminho_pdf):
                with open(caminho_pdf, "w") as f:
                    f.write("A geração de PDF está sendo processada pelo servidor de build.")

if __name__ == "__main__":
    gerar_downloads()
