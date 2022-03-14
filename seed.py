import pandas as pd
import numpy as np
import bd

def register_estados(df):
    estados = df.drop_duplicates(subset = ['c_estado'])
    for index in estados.index:
        c_estado = df.loc[index].at['c_estado']
        d_estado = df.loc[index].at['d_estado']
        bd.insert_estado(c_estado, d_estado)
    return

def register_municipios(df):
    municipios = df.drop_duplicates(subset = ['c_mnpio', 'c_estado'])
    municipios = municipios.fillna(0)
    for index in municipios.index:
    #try:
        c_mnpio = df.loc[index].at['c_mnpio']
        c_estado = df.loc[index].at['c_estado']
        D_mnpio = df.loc[index].at['D_mnpio']
        d_ciudad = df.loc[index].at['d_ciudad']
        c_cve_ciudad = df.loc[index].at['c_cve_ciudad']
        bd.insert_municipio(c_mnpio, c_estado, D_mnpio, d_ciudad, c_cve_ciudad)
    #except:
        #print(df.loc[index,['c_mnpio','c_estado','D_mnpio','d_ciudad','c_cve_ciudad']])
    return

def register_admin_postal(df):
    admin_postal = df.drop_duplicates(subset = ['d_CP'])
    for index in admin_postal.index:
        d_CP = df.loc[index].at['d_CP']
        c_oficina = df.loc[index].at['c_oficina']
        bd.insert_admin_postal(d_CP, c_oficina)
    return

def register_colonias(df):
    colonias = df.drop_duplicates(subset = ['id_asenta_cpcons'])
    for index in colonias.index:
        d_codigo = colonias.loc[index].at['d_codigo']
        c_mnpio = colonias.loc[index].at['c_mnpio']
        c_estado = colonias.loc[index].at['c_estado']
        d_CP = colonias.loc[index].at['d_CP']
        d_asenta = colonias.loc[index].at['d_asenta']
        c_tipo_asenta = colonias.loc[index].at['c_tipo_asenta']
        id_asenta_cpcons = colonias.loc[index].at['id_asenta_cpcons']
        d_zona = colonias.loc[index].at['d_zona']
        d_tipo_asenta = colonias.loc[index].at['d_tipo_asenta']
        bd.insert_colonia(d_codigo, c_mnpio, c_estado, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta)
    return

def fill_info(path):
    df = pd.read_csv(path, sep = '|', skiprows = 1, encoding= "latin1")
    register_estados(df)
    register_municipios(df)
    register_admin_postal(df)
    register_colonias(df)
    return



if __name__ == "__main__":
    bd.clear_tables()
    fill_info("./docs/CPdescarga.txt")
