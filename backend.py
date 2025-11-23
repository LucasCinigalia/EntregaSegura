import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

def configurar_ia():
    if not api_key:
        raise ValueError("A chave da API não foi encontrada.")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

def analisar_imagem(imagem):
    model = configurar_ia()

    prompt = """
    Aja como um Especialista em Segurança Viária do iFood.
    Analise a imagem fornecida e gere um JSON PURO (sem formatação markdown) com:
    
    {
        "risco": "BAIXO/MÉDIO/ALTO",
        "motivo": ["motivo 1", "motivo 2"],
        "recomendacao": "Recomendação curta"
    }

    Foque em: Iluminação, estado da via (buracos), trânsito, clima e segurança pessoal.
    Se a imagem não for de uma rua/trânsito, responda que não foi possível identificar o cenário.
    """

    try:
        response = model.generate_content([prompt, imagem])
        texto_resposta = response.text
        texto_limpo = texto_resposta.replace("```json", "").replace("```", "")
        return texto_limpo
    except Exception as e:
        return f"Erro ao analisar imagem: {str(e)}"

