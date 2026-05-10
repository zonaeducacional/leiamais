import os
import yaml
import subprocess

def processar():
    pasta_importar = "content/importar"
    if not os.path.exists(pasta_importar):
        return

    arquivos = [f for f in os.listdir(pasta_importar) if f.endswith(".md")]
    
    if not arquivos:
        print("Nenhuma nova importação pendente.")
        return

    for arquivo in arquivos:
        caminho = os.path.join(pasta_importar, arquivo)
        print(f"Processando pedido: {arquivo}")
        
        with open(caminho, "r", encoding="utf-8") as f:
            # Extrai o frontmatter (o YAML no topo do arquivo)
            try:
                conteudo = f.read().split("---")[1]
                dados = yaml.safe_load(conteudo)
                
                # Chama o seu script de importação original
                cmd = [
                    "python3", "importar_livro.py",
                    str(dados["gutenberg_id"]),
                    dados["title"],
                    dados["autor"],
                    dados["ano"],
                    dados["categoria"]
                ]
                subprocess.run(cmd, check=True)
                
                # Remove o pedido para não processar de novo
                os.remove(caminho)
                print(f"✅ Livro '{dados['title']}' importado com sucesso!")
                
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

if __name__ == "__main__":
    processar()
