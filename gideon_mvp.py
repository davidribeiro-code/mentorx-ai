import streamlit as st
import ollama

# Configuração da página
st.set_page_config(page_title="MentorX AI - Gideon", page_icon="🤖")

st.title("🤖 Gideon - O teu Mentor de Carreira")
st.write("Bem-vindo ao MentorX AI! Estou aqui para estruturar o teu plano de desenvolvimento profissional.")

# Inicializar histórico de chat na memória da sessão
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá, David! Sou o Gideon. Que competência digital gostarias de desenvolver hoje?"}
    ]

# Mostrar mensagens anteriores do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do utilizador
if user_input := st.chat_input("Digita a tua dúvida sobre carreira ou tecnologia..."):
    # 1. Adicionar a pergunta do utilizador ao histórico e mostrar na tela
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # 2. Chamar o modelo local do Ollama em tempo real
    with st.chat_message("assistant"):
        with st.spinner("O Gideon está a pensar..."):
            try:
                response = ollama.chat(
                    model="gideon",  # Usa o teu modelo listado no terminal
                    messages=st.session_state.messages # Passa o histórico para ele ter contexto
                )
                gideon_response = response['message']['content']
            except Exception as e:
                gideon_response = f"Erro ao conectar ao Ollama: {str(e)}. Garante que o serviço está ativo."
        
        # 3. Mostrar a resposta real da IA e guardar no histórico
        st.markdown(gideon_response)
    st.session_state.messages.append({"role": "assistant", "content": gideon_response})