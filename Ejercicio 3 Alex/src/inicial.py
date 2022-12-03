''' 
1. Importar las librerias
Pandas: Especializada en el manejo y analisis de estructuras de datos
os: Funcionalidades de sistema operativo.
pathlib: Manipular rutas
'''
import pandas as pd
import os
from pathlib import Path

#Variables de ruta
root_dir = Path(__file__).parent.resolve().parent #Path(__file__).parent=Carpeta Script - parent lleva una carptea atras de donde estamos
file_name = "MOCK_DATA.csv"
file_path = os.path.join(root_dir,"data","raw",file_name)#Ruta completa del archivo


#EXTRACION Crear Data Frame
df = pd.read_csv(file_path, sep=";")#Cargar csv en un dataframe con Pandas, sep indica el caracter de separacion del archivo



#TRANSFORMACION DataFrame
#Cantidad de datos unicos por cada columna
'''
df.dtypes: Tipos de datos del dataframe
df.shape: Cantidad de filas y columnas. df.shape[0] = Filas. df.shape[1] = Columnas
df.head(10): Primeros 10 registros
df.tail(10): Ultmios 10 registros
df["gender"].value_counts(): Generos y cantidad de perosnas con x genero. value_counts("normalize=True") = Normalizar
df["gender"].unique() = Valores unicos
len(df["gender"].unique()) = Total valores unicos
'''
list_col= df.columns # Crear lista de columnas de df

new_table = dict()  #Crear diccionario

for col  in (list_col):
    list_unicos = df[col].unique() #Listado de unicos
    longitud =  len(list_unicos) #Cantidad de cada unico
    new_table[col] = longitud #Llenado de diccionario donde la key es la columna y la llave es la cantidad de unico


reporte = pd.DataFrame.from_dict(new_table, orient="index") #Convertir diccionario en DataFrame

reporte.rename({0:"Conteo"}, axis=1, inplace=True) #Renombrar segunda columna con "Conteo"

reporte.reset_index(inplace=True) #Resetear index


#CARGA

final_name_output = "reporte_"+ file_name #Nombre del archiovo exportado
final_output = os.path.join(root_dir,"data","process",final_name_output)# Ruta del archivo exportado

reporte.to_csv(final_output) #Exportar DataFrame a CSV 
print("Exitoooo")