"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Eliminar filas con valores nulos o vacíos
    df = df.dropna()

    # Convertir columnas relevantes a tipos de datos adecuados
    df['sexo'] = df['sexo'].str.upper()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype(str).str.upper()
    df['idea_negocio'] = df['idea_negocio'].astype(str).str.replace('-', ' ').str.replace('_', ' ').str.upper()
    df['barrio'] = df['barrio'].astype(str).str.lower()
    df['estrato'] = df['estrato'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])
    df['línea_credito'] = df['línea_credito'].str.upper()

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    return df
