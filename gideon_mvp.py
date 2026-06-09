import streamlit as st

# Configuração da página
st.set_page_config(page_title="MentorX AI - Gideon", page_icon="🤖")

st.title("🤖 Gideon - O teu Mentor de Carreira")
st.write("Bem-vindo ao MentorX AI! Estou aqui para estruturar o teu plano de desenvolvimento profissional.")

# Inicializar histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá, David! Sou o Gideon. Que competência digital gostarias de desenvolver hoje?"}
    ]

# Mostrar mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do utilizador
if user_input := st.chat_input("Digita a tua dúvida sobre carreira ou tecnologia..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # Resposta simulada do Gideon baseada na tua stack
    gideon_response = f"Excelente escolha! Para desenvolveres '{user_input}', o melhor caminho inicial é focar em algoritmos com Python e arquitetura de sistemas."
    
    st.session_state.messages.append({"role": "assistant", "content": gideon_response})
    with st.chat_message("assistant"):
        st.markdown(gideon_response)