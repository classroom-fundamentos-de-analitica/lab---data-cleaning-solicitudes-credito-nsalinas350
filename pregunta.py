"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
from datetime import datetime
import re


import pandas as pd

def clean_data():
  df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
  df.dropna(inplace=True)
  df.fecha_de_beneficio = [datetime.strptime(i, "%d/%m/%Y") if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", i))
  else datetime.strptime(i, "%Y/%m/%d")
  for i in df.fecha_de_beneficio]
  # df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True, errors='coerce')
  df.barrio = [str.lower(i).replace("_", " ").replace("-", " ") for i in df.barrio]
  df.sexo = df.sexo.str.lower()
  df.idea_negocio = [str.lower(i.replace("_", " ").replace("-", " ")) for i in df.idea_negocio]
  df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
  df.estrato = df.estrato.astype(int)
  df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
  df.línea_credito = df.línea_credito.str.replace('-', ' ').str.replace('_', ' ').str.upper()
  df.monto_del_credito = [int(i.replace("$ ", "").replace(".00", "").replace(",", "")) for i in
                          df.monto_del_credito]
  df.drop_duplicates(inplace=True)
  return df
