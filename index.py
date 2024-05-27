import streamlit as st

with st.sidebar:
  st.title("Calculadora IMC")
  st.header("IMC: Definição?")

  st.write("Índice de Massa Corporal (IMC).")

  st.write("É um índice que relaciona peso e altura de uma pessoa.")

  st.write("É utilizado como medidia de saúde geral e para determinar se um apessoa está em um peso ideal.")

st.title("Calculadora")

peso = st.number_input(label="Digite seu peso em Kg", min_value=0.0)
altura = st.number_input(label="Digite sua altura", min_value=0.0, max_value=2.90)

if st.button("Calcular"):
  imc = peso / (altura**2)
  imc_ideal = 21.7
  imc_delta = imc - imc_ideal

  if imc < 18.5:
    resultado = {
      "classe": 'baixo peso',
      "delta": imc_delta
    }
  elif 18.5 <= imc < 25:
    resultado = {
      "classe": 'Peso ideal',
      "delta": imc_delta
    }
  elif 25 <= imc <= 30:
    resultado = {
      "classe": 'Sobrepeso',
      "delta": imc_delta
    }
  elif imc <= 40:
    resultado = {
      "classe": 'obesidade',
      "delta": imc_delta
    }
  else:
    resultado = {
      "classe": 'obesidade morbida',
      "delta": imc_delta
    }
  st.code(f"O resultado é {resultado}")

  col1, col2 = st.columns(2)

  col1.metric("IMC classificado", resultado["classe"], resultado["delta"], delta_color="off")
  col2.metric("IMC calculado", round(imc, 2), resultado["delta"], delta_color="off")

  st.divider()
  st.text("Fonte")