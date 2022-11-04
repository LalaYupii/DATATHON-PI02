'''
Funciones para ML
Fecha: 30-10-2022
Autor: Lala Yupii
'''


import pandas as pd



def valoresFaltantes(df):
    '''
    Devuelve un DataFrame con los porcentajes de nulos por columna
    
    df: DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    # Nulos
    nulos = df.isnull().sum()

    #Ordenamos
    nulos = nulos.sort_values(nulos[1], ascending=False)

    #Calculamos porcentaje en relación al total del DataFrame
    nulos = nulos.apply(lambda x : x / total * 100)

    # Seteamos la cantidad de filas de salida según el DataFrame
    # para poder visualizar toda la data
    pd.set_option('display.max_rows', nulos.shape[0])

    return nulos






def valoresUnicos(df):
    '''
    Devuelve el porcentaje de valores únicos por columna de un DataFrame
    df: DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    # Únicos
    unicos = df.nunique()

    #Ordenamos
    unicos = unicos.sort_values(ascending=False)

    #Calculamos porcentaje en relación al total del DataFrame
    unicos = unicos.apply(lambda x : x / total * 100)

    # Seteamos la cantidad de filas de salida según el DataFrame
    # para poder visualizar toda la data
    pd.set_option('display.max_rows', unicos.shape[0])

    return unicos






def valoresOutliers(df, col):
    '''
    Devuelve el porcentaje de outliers por columna del DataFrame
    
    df: DataFrama a procesar
    col -> str: columna del DataFrame a analizar
    '''
    # Tamaño total del DataFrame
    total = df.shape[0]

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    BI = Q1 - 1.5 * IQR
    BS = Q3 + 1.5 * IQR

    ol = df[(df[col] < BI) | (df[col] > BS)].shape[0]

    return ol / total * 100


