"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    # Cargar los datos
    df = pd.read_csv('datos.csv')

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Eliminar filas con valores nulos o vacíos
    df = df.dropna()

    # Convertir columnas relevantes a tipos de datos adecuados
    df['sexo'] = df['sexo'].astype(str)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype(str)
    df['idea_negocio'] = df['idea_negocio'].astype(str)
    df['barrio'] = df['barrio'].astype(str)
    df['estrato'] = df['estrato'].astype(int)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])

    return df
