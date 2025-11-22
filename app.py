import streamlit as st
from agents.multi_tool_agent import MultiToolAgent
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Financial AI Agent", layout="centered")

# --- Estilo CSS ---
st.markdown("""
    <style>
        .response-card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #333;
            color: #e0e0e0;
            font-size: 1.1rem;
            margin-top: 20px;
            line-height: 1.6;
        }
        .stTextInput label {
            font-size: 1.1rem !important;
        }
        .stButton>button {
            background-color: #4a4a4a;
            color: white;
            border-radius: 8px;
            padding: 8px 20px;
            border: none;
            font-size: 1.05rem;
        }
        .stButton>button:hover {
            background-color: #6b6b6b;
        }
    </style>
""", unsafe_allow_html=True)

# --- Interface ---
st.title("💹 Financial AI Agent — Dashboard")
st.write("Faça perguntas sobre **CDI, IPCA, SELIC e investimentos**.")

agent = MultiToolAgent()

query = st.text_input("Pergunte:")

if st.button("Enviar"):

    with st.spinner("Consultando agente..."):
        result = agent.run(query)

    # pega só o texto da resposta
    try:
        agent_message = result.output_text()
    except:
        agent_message = result.content if hasattr(result, "content") else str(result)

    # Exibe bonito
    st.markdown(
        f"<div class='response-card'>{agent_message}</div>",
        unsafe_allow_html=True
    )
