import bd

def get_all_estados():
    json = {"estados": []}
    estados = bd.get_estados()
    for e in estados:
        json['estados'].append({"c_estado": e[0], "d_estado": e[1]})
    return json

def get_all_municipios():
    json = {"municipios": []}
    municipios = bd.get_municipios()
    for m in municipios:
        json['municipios'].append({"c_mnpio": m[0], "c_estado": m[1], "D_mnpio": m[2], "d_ciudad": m[3], "c_cve_ciudad": m[4]})
    return json

def get_all_colonias():
    json = {"colonias": []}
    colonias = bd.get_colonias()
    for c in colonias:
        json['colonias'].append({"d_codigo": c[0], "c_mnpio": c[1], "c_estado": c[2], "d_CP": c[3], "d_asenta": c[4], "c_tipo_asenta": c[5], "id_asenta_cpcons": c[6], "d_zona": c[7], "d_tipo_asenta": c[8]})
    return json

def get_all_admin_postal():
    json = {"admin_postal": []}
    admin_postal = bd.get_admin_postal()
    for a in admin_postal:
        json['admin_postal'].append({"d_CP": a[0], "c _oficina": a[1]})
    return json

def get_colonias_cp(cp):
    json = {"colonias": []}
    colonias = bd.get_colonias_cp(cp)
    for c in colonias:
        json['colonias'].append({"d_codigo": c[0], "c_mnpio": c[1], "c_estado": c[2], "d_CP": c[3], "d_asenta": c[4], "c_tipo_asenta": c[5], "id_asenta_cpcons": c[6], "d_zona": c[7], "d_tipo_asenta": c[8]})
    return json





#print(get_colonias_cp(1001))