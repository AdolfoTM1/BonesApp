df_femur = pd.read_excel('FEMUR.xlsx', sheet_name='Femur') # Added decimal=',' to handle comma as decimal separator
df_tibia = pd.read_excel('FEMUR.xlsx', sheet_name='Tibia') # Added decimal=',' to handle comma as decimal separator
df_humero = pd.read_excel('FEMUR.xlsx', sheet_name='Humero') # Added decimal=',' to handle comma as decimal separator

# Entrenar modelos para cada hueso
def entrenar_modelo(df):
  X = df.drop('Especie ', axis=1)
  y = df['Especie ']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  rfc = RandomForestClassifier(random_state=42)
  rfc.fit(X_train, y_train)
  return rfc

modelo_femur = entrenar_modelo(df_femur)
modelo_tibia = entrenar_modelo(df_tibia)
modelo_humero = entrenar_modelo(df_humero)

# Interfaz Streamlit
st.title("Sistema de Predicción de Especies")

hueso = st.selectbox("Seleccione el hueso:", ["Fémur", "Tibia", "Húmero"])

if hueso == "Fémur":
  longitud = st.number_input("Ingrese la Long. Máxima:")
  diametro_ap = st.number_input("Ingrese el Diámetro anteroposterior (pto. medio):")
  diametro_ml = st.number_input("Ingrese el Diámetro medio lateral (pto. medio):")
  perimetro_pm = st.number_input("Ingrese el perímetro pto medio:")
  diametro_subtro_ap = st.number_input("Ingrese el Dmtro. Subtrocanterico antero posterior:")
  diametro_subtro_ml = st.number_input("Ingrese el Dmtro. Subtro medio lateral:")
  perimetro_subtro = st.number_input("Ingrese el perímetro subtro:")
  perimetro_foramen = st.number_input("Ingrese el Perímetro foramen nutricio:")
  diametro_cabeza = st.number_input("Ingrese el diámetro max. Cabeza:")

  if st.button("Predecir"):
    nuevo_hueso = pd.DataFrame({
        'Long. Máxima': [longitud],
        'Diámetro anteroposterior (pto. medio)': [diametro_ap],
        'Diámetro medio lateral (pto. medio)': [diametro_ml],
        'perímetro pto medio': [perimetro_pm],
        'Dmtro. Subtrocanterico antero posterior': [diametro_subtro_ap],
        'Dmtro. Subtro medio lateral': [diametro_subtro_ml],
        'perímetro subtro': [perimetro_subtro],
        'Perímetro foramen nutricio': [perimetro_foramen],
        'diámetro max. Cabeza': [diametro_cabeza]
    })
    prediccion = modelo_femur.predict(nuevo_hueso)
    st.success(f"La especie predicha es: {prediccion[0]}")


elif hueso == "Tibia":
  longitud = st.number_input("Ingrese la Long. Máxima:")
  diametro_ap = st.number_input("Ingrese el dmtro. antero-posterior del pto medio:")
  diametro_ml = st.number_input("Ingrese el dmtro. Medio - lateral a nivel del pto medio:")
  circunferencia_pm = st.number_input("Ingrese la circumferencia del pto medio:")
  diametro_ap_foramen = st.number_input("Ingrese el dmtro. Antero - posterio foramen nutricio:")
  diametro_ml_foramen = st.number_input("Ingrese el dmtro. Medio-lateral foramen nutricio:")
  circunferencia_foramen= st.number_input("Ingrese la circunferencia foramen nutricio:")
 
  if st.button("Predecir"):
    nuevo_hueso = pd.DataFrame({
        'Long. Máxima':[longitud], 
        'dmtro. antero-posterior del pto medio':[diametro_ap],
        'dmtro. Medio - lateral a nivel del pto medio': [diametro_ml],
        'circumferencia del pto medio':[circunferencia_pm],
        'dmtro. Antero - posterio foramen nutricio':[diametro_ap_foramen],
        'dmtro. Medio-lateral foramen nutricio':[diametro_ml_foramen],
        'circunferencia foramen nutricio':[circunferencia_foramen]
    })
    prediccion = modelo_tibia.predict(nuevo_hueso)
    st.success(f"La especie predicha es: {prediccion[0]}")

elif hueso == "Húmero":
  longitud = st.number_input("Ingrese la Longitud máxima:")
  diametro_ap = st.number_input("Ingrese el diámetro antero -posterior del pto medio:")
  diametro_ml = st.number_input("Ingrese el diámetro medio-lateral del pto medio:")
  circunferencia_pm = st.number_input("Ingrese la circunferencia del pto medio:")
  circunferencia_foramen = st.number_input("Ingrese la circunferencia a la altura del foramen nutricio:")
  diametro_cabeza = st.number_input("Ingrese el diámetro cabeza:")

  if st.button("Predecir"):
    nuevo_hueso = pd.DataFrame({
        'Longitud máxima': [longitud],
        'diámetro antero -posterior del pto medio': [diametro_ap],
        'diámetro medio-lateral del pto medio': [diametro_ml],
        'circunferencia del pto medio': [circunferencia_pm],
        'circunferencia a la altura del foramen nutricio': [circunferencia_foramen],
        'diámetro cabeza': [diametro_cabeza]
    })
    prediccion = modelo_humero.predict(nuevo_hueso)
    st.success(f"La especie predicha es: {prediccion[0]}")
