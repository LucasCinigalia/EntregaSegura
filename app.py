from PIL import Image
import streamlit as st # type: ignore
import backend
import json
import time

st.set_page_config(page_title="SafeRider AI", page_icon="🛵", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #EA1D2C;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #c2101e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛵 SafeRider.AI")
st.markdown("### Copiloto de segurança para entregadores")
st.info("Sistema de GenIA que analisa a imagem da sua rua e te dá uma recomendação de segurança.")

st.divider()

uploaded_file = st.file_uploader("Envie uma foto da rua: ", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Visão do Entregador", use_container_width=True)

    if st.button("Analisar segurança"):
        progress_text = "Analisando a imagem"
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        try:
            resultado_texto = backend.analisar_imagem(image)
            dados = json.loads(resultado_texto)
            
            my_bar.empty()

            st.markdown("---")
            st.subheader("Resultado da análise")

            risco = dados.get("risco", "Desconhecido").upper()

            col1, col2 = st.columns([1, 2])

            with col1:
                if risco == "ALTO":
                    st.error(f"Risco: {risco}")
                elif risco == "MÉDIO":
                    st.warning(f"Risco: {risco}")
                else:
                    st.success(f"Risco: {risco}")

            with col2:
                st.markdown("**Recomendação Imediata:**")
                st.write(f"_{dados.get("recomendacao")}_")

            with st.expander("Ver detalhes dos perigos", expanded=True):
                for motivo in dados.get("motivo", []):
                    st.markdown(f"- {motivo}")

        except Exception as e:
            st.error(f"Erro ao analisar a imagem: {str(e)}")
            st.write(resultado_texto)

st.markdown("---")
st.caption("Projeto desenvolvido para o processo seletivo do Ifood | GenIA")