import pymysql

def get_conn():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='sepomex')

def insert_estado(c_estado, d_estado):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Estado(c_estado, d_estado) VALUES (%s, %s)",
                       (c_estado, d_estado))
    conn.commit()
    conn.close()

def insert_admin_postal(d_CP, c_oficina):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Admin_postal(d_CP, c_oficina) VALUES (%s, %s)",
                       (d_CP, c_oficina))
    conn.commit()
    conn.close()

def insert_municipio(c_mnpio, c_estado, D_mnpio, d_ciudad, c_cve_ciudad):
    conn = get_conn()
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Municipio(c_mnpio, c_estado, D_mnpio, d_ciudad, c_cve_ciudad) VALUES (%s, %s, %s, %s, %s)",
                        (c_mnpio, c_estado, D_mnpio, d_ciudad, c_cve_ciudad))
        except:
            cursor.execute("INSERT INTO Municipio(c_mnpio, c_estado, D_mnpio, d_ciudad) VALUES (%s, %s, %s, %s)",
                        (c_mnpio, c_estado, D_mnpio, D_mnpio))
    conn.commit()
    conn.close()

def insert_colonia(d_codigo, c_mnpio, c_estado, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Colonia(d_codigo, c_mnpio, c_estado, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (d_codigo, c_mnpio, c_estado, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta))
    conn.commit()
    conn.close()

def get_estados(): 
    conn = get_conn()
    estados = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Estado")
        estados = cursor.fetchall()
    conn.close()
    return estados

def get_municipios(): 
    conn = get_conn()
    municipios = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Municipio")
        municipios = cursor.fetchall()
    conn.close()
    return municipios

def get_colonias(): 
    conn = get_conn()
    colonias = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Colonia")
        colonias = cursor.fetchall()
    conn.close()
    return colonias

def get_admin_postal(): 
    conn = get_conn()
    admin_postal = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Admin_postal")
        admin_postal = cursor.fetchall()
    conn.close()
    return admin_postal

def update_estado(c_estado, d_estado):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE Estado SET d_estado = %s WHERE c_estado = %s",
                       (d_estado, c_estado))
    conn.commit()
    conn.close()

def update_municipio(c_mnpio, c_estado, D_mnpio, d_ciudad, c_cve_ciudad):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE Municipio SET c_estado = %s, D_mnpio = %s, d_ciudad = %s, c_cve_ciudad = %s WHERE c_mnpio = %s",
                       (c_estado, D_mnpio, d_ciudad, c_cve_ciudad, c_mnpio))
    conn.commit()
    conn.close()

def update_colonia(d_codigo, c_mnpio, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE Colonia SET c_mnpio = %s, d_CP = %s, d_asenta = %s, c_tipo_asenta = %s, id_asenta_cpcons = %s, d_zona = %s, d_tipo_asenta = %s WHERE d_codigo = %s",
                       (c_mnpio, d_CP, d_asenta, c_tipo_asenta, id_asenta_cpcons, d_zona, d_tipo_asenta, d_codigo))
    conn.commit()
    conn.close()

def update_admin_postal(d_CP, c_oficina):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE Admin_postal SET c_oficina = %s WHERE d_CP = %s",
                       (c_oficina, d_CP))
    conn.commit()
    conn.close()

def delete_estado(c_estado):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Estado WHERE c_estado = %s", (c_estado))
    conn.commit()
    conn.close()

def delete_municipio(c_mnpio):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Municipio WHERE c_mnpio = %s", (c_mnpio))
    conn.commit()
    conn.close()

def delete_colonia(c_codigo):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Colonia WHERE c_codigo = %s", (c_codigo))
    conn.commit()
    conn.close()

def delete_admin_postal(d_CP):
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Admin_postal WHERE d_CP = %s", (d_CP))
    conn.commit()
    conn.close()

def clear_tables():
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Colonia;")
        cursor.execute("DELETE FROM Municipio;")
        cursor.execute("DELETE FROM Admin_postal;")
        cursor.execute("DELETE FROM Estado;")
    conn.commit()
    conn.close()

def get_estado_id(id):
    conn = get_conn()
    estado = None
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Estado WHERE c_estado = %s", (id))
        estado = cursor.fetchone()
    conn.close()
    return estado

def get_colonias_cp(cp):
    conn = get_conn()
    colonias = None
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM Colonia WHERE d_CP = %s", (cp))
        colonias = cursor.fetchall()
    conn.close()
    return colonias