import os
os.system("cls")

es_valido = False
CONSULTA_MEDICA = 25000
ATENCION_URGENCIA = 45000
EXAMEN_MEDICO = 30000




nombre_paciente = input("Ingrese su nombre: ")
edad_paciente = int(input("Ingrese su edad: "))
tipo_atencion = int(input("Ingrese tipo de atencion. 1.-Consulta Medica  2.-Atencion de urgencia  3.-Examen Medico: "))

if tipo_atencion >= 1 and tipo_atencion <= 3:
    es_valido = True
    
if es_valido:
    print("voy bien")
    #desclasificare el tipo de atencion
    if tipo_atencion == 1:
        atencion = "Consulta medica"
        atencion_str = "Atencion programada: "
        precio_atencion = CONSULTA_MEDICA
        descuento = 0.20
    elif tipo_atencion == 2:
        atencion = "Atencion de Urgencia"
        atencion_str = "Atencion prioritaria"
        precio_atencion = ATENCION_URGENCIA
    else:
        atencion = "Examen Medico"
        atencion_str = "Atencion de diagnostico"
        precio_atencion = EXAMEN_MEDICO
        
    if edad_paciente <=12:
        descuento = 0.20
    elif edad_paciente >= 12 and edad_paciente <=64:
        descuento = 0.15
    else:
        descuento = 0.15
    
    valor_descuento = precio_atencion * descuento
    valor_final = precio_atencion - valor_descuento

else:
    print("Tipo de atencion no valido: ")
    #la app se detiene
    

print(f"""
Paciente: {nombre_paciente}      
Edad: {edad_paciente}
Tipo de atencion: {atencion}
Descuento: {valor_descuento}
Total a pagar: {valor_final}


""")
