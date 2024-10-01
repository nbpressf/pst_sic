import streamlit as st

def calcIMC():
    IMC =  lambda peso, altura: peso/(altura**2)
    st.title("Calculadora de IMC")
    #st.latex("")
    #st.image("")
    peso = st.number_input("Entrada de Peso: ",min_value=0.00)
    altura = st.number_input("Entrada de Altura: ", min_value=0.00)
    if peso and altura:
        IMC_atual = IMC(peso,altura)
        st.text(f"Seu IMC é de {round(IMC(peso, altura))}.")
        if IMC_atual < 20:
            IMC_atual = "Abaixo do Peso."
        elif IMC_atual < 25: 
            IMC_atual = "Peso Normal"
        elif IMC_atual < 30:
            IMC_atual = "Excesso de Peso"
        elif IMC_atual < 35:
            IMC_atual = "Obesidade"
        else:
            IMC_atual = "Super Obesidade"
    else:
        st.text("Não foi dado os valores")
    st.text("De acordo com a tabela, você se encaixa em {IMC_atual}")

calcIMC()

st.title("Atividade 1 - streamlit")
with st.expander("IMC calculadora"):
    calcIMC()

