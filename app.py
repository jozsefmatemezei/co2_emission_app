import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="CO2-kibocsátás Becslő App",
    layout="wide"
)

model = joblib.load('forest_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("CO2-kibocsátás Becslő Applikáció")
st.markdown("""
Ez az alkalmazás egy betanított modell segítségével jósolja meg a gépjárművek CO2-kibocsátását.
""")
st.markdown("---")

st.header("Új autó kibocsátásának becslése")

col_input, col_result = st.columns([2, 1])

with col_input:
    st.subheader("Adatok megadása")
    engine_size = st.slider("Motor mérete (L)", min_value=1.0, max_value=8.4, value=2.0, step=0.1)
    cylinders = st.slider("Hengerek száma", min_value=3, max_value=16, value=4, step=1)
    fuel_consumption = st.number_input("Kombinált üzemanyag fogyasztás (L/100 km)", min_value=3.0, max_value=30.0, value=8.5, step=0.1)

with col_result:
    st.subheader("Eredmény")
    st.write("Kattintson a gombra a becsléshez:")
     
    if st.button("Számítás indítása", use_container_width=True):
        input_data = np.array([[engine_size, cylinders, fuel_consumption]])
        input_scaled = scaler.transform(input_data)
        
        prediction = model.predict(input_scaled)
        
        st.metric(
            label="Becsült CO2-kibocsátás", 
            value=f"{prediction[0]:.2f} g/km",
            delta="Sikeres számítás!", delta_color="normal"
        )
       
    else:
        st.info("Adja meg az adatokat a bal oldalon, majd nyomja meg a gombot!")