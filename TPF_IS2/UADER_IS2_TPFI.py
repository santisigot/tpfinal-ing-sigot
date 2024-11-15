import uuid
from InterfazParaAWS import InterfazParaAWS

# Función principal que simula la ejecución del sistema
if __name__ == "__main__":
    # Generar UUIDs para simular sesiones y CPU
    uuid_session = str(uuid.uuid4())
    uuid_cpu = str(uuid.getnode())
    id_sede = "UADER-FCyT-IS2"        

    # Crear instancia de la interfaz
    interfaz = InterfazParaAWS(uuid_session, uuid_cpu) 
    
    i2 = InterfazParaAWS(uuid_session, uuid_cpu)
    
    if i2 == interfaz:
        print("es singleton")
    else: print("no es singleton")

    # Obtener datos de la sede
    print("Datos de la sede:", interfaz.consultar_datos_sede(uuid_session, uuid_cpu, id_sede))

    # Obtener CUIT de la sede
    print("CUIT de la sede:", interfaz.consultar_cuit(uuid_session, uuid_cpu, id_sede))

    # Obtener ID de secuencia de la sede
    print("ID de Secuencia:", interfaz.generar_id_secuencia(uuid_session, uuid_cpu, id_sede))

    # Registrar una acción en el log
    action = "Consulta de datos de sede"
    status = "Éxito"
    print("Registrando acción en CorporateLog...")
    print(interfaz.registrar_log())
    
    # print(interfaz.es_singleton())
    # Listar los logs
    print("Listado de CorporateLog:", interfaz.listar_logs(filtro="cpu"))
