import backend
from PIL import Image
import os
import json

NOME_IMAGEM = "rua_teste.jpg"

def rodar_teste():
    if not os.path.exists(NOME_IMAGEM):
        print(f"Arquivo {NOME_IMAGEM} não encontrado.")
        return

    try:
        imagem = Image.open(NOME_IMAGEM)
        resposta = backend.analisar_imagem(imagem)
        print("Resposta da IA:")
        print(resposta)

        try:
            dados = json.loads(resposta)
            print(f"Risco: {dados.get("risco")}")
            print(f"Motivo: {dados.get("motivo")}")
            print(f"Recomendação: {dados.get("recomendacao")}")
        except:
            print("Formato de resposta inválido")
        
    except Exception as e:
        print(f"Erro ao analisar imagem: {str(e)}")

if __name__ == "__main__":
    rodar_teste()