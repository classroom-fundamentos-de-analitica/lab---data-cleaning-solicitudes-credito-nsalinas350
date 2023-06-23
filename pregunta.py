"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
  df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

  # Eliminar filas con valores nulos o vacíos
  df.dropna(inplace=True)

  # Convertir columnas
  df.sexo = df.sexo.str.upper()
  df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.astype(str).str.upper()
  df.idea_negocio = df.idea_negocio.astype(str).str.replace('-', ' ').str.replace('_', ' ').str.upper()
  df.barrio = df.barrio.str.replace('-', ' ').str.replace('_', ' ').astype(str).str.lower()
  df.estrato = df.estrato.astype(int)
  df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
  df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, format='%d/%m/%Y', errors='coerce').fillna(
    pd.to_datetime(df.fecha_de_beneficio, format='%Y/%m/%d', errors='coerce'))
  df.monto_del_credito = df.monto_del_credito.replace('[\$,]', '', regex=True).astype(float)
  df.línea_credito = df.línea_credito.str.replace('-', ' ').str.replace('_', ' ').str.upper()

  # Eliminar filas duplicadas
  df.drop_duplicates(inplace=True)
  return df
