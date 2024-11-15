import json
from decimal import Decimal
from CorporateLog import CorporateLog
from CorporateData import CorporateData
from singleton import SingletonMeta
# Función para convertir objetos Decimal a float
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # Convertir Decimal a float
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")

class InterfazParaAWS(metaclass=SingletonMeta):
    def __init__(self, session_id, cpu_id):
        self.session_id = session_id
        self.cpu_id = cpu_id
        self.log_instance = CorporateLog.getInstance()
        self.data_instance = CorporateData.getInstance()

        self.data_instance_2 = CorporateData.getInstance()

        self.es_singleton()

    def es_singleton(self):    
        if self.data_instance is self.data_instance_2:
            return "es singleton"
        else:
            return "no es singleton"

    def registrar_log(self):
        result = self.log_instance.post(self.session_id)
        return json.dumps({"resultado_registro": result}, default=decimal_default)

    def consultar_datos_sede(self, session_id, cpu_id, sede_id):
        # Pasar los tres parámetros a getData
        data = self.data_instance.getData(session_id, cpu_id, sede_id)
        return json.dumps({"datos_sede": data}, default=decimal_default)

    def consultar_cuit(self, session_id, cpu_id, sede_id):
        # Pasar los tres parámetros a getCUIT
        cuit = self.data_instance.getCUIT(session_id, cpu_id, sede_id)
        return json.dumps({"cuit": cuit}, default=decimal_default)

    def generar_id_secuencia(self, session_id, cpu_id, sede_id):
        # Pasar los tres parámetros a getSeqID
        new_seq_id = self.data_instance.getSeqID(session_id, cpu_id, sede_id)
        return json.dumps({"nuevo_id_secuencia": int(new_seq_id["idSeq"])}, default=decimal_default)

    def listar_logs(self, filtro="cpu"):
        logs = self.log_instance.list()

        if filtro == "cpu":
            return json.dumps({"logs_por_cpu": logs}, default=decimal_default, indent=4)
        elif filtro == "session":
            logs_filtrados = [log for log in logs if log["sessionid"] == self.session_id]
            return json.dumps({"logs_por_sesion": logs_filtrados}, default=decimal_default, indent=4)
        else:
            return json.dumps({"error": "Filtro no válido. Use 'cpu' o 'session'."}, default=decimal_default)

    # Método para listar todos los datos de CorporateData para un id_sede
    def listar_corporate_data(self, sede_id):
        # Obtenemos los datos para el id_sede
        data = self.data_instance.list(sede_id)
        return json.dumps({"datos_sede": data}, default=decimal_default, indent=4)

# import json
# from decimal import Decimal
# from CorporateLog import CorporateLog
# from CorporateData import CorporateData

# # Función para convertir objetos Decimal a float
# def decimal_default(obj):
#     if isinstance(obj, Decimal):
#         return float(obj)  # Convertir Decimal a float
#     raise TypeError(f"Type {obj.__class__.__name__} not serializable")

# class InterfazParaAWS:
#     def __init__(self, session_id, cpu_id):
#         self.session_id = session_id
#         self.cpu_id = cpu_id
#         self.log_instance = CorporateLog.getInstance()
#         self.data_instance = CorporateData.getInstance()

#     def registrar_log(self):
#         result = self.log_instance.post(self.session_id)
#         return json.dumps({"resultado_registro": result})

#     def consultar_datos_sede(self, session_id, cpu_id, sede_id):
#         # Pasar los tres parámetros a getData
#         data = self.data_instance.getData(session_id, cpu_id, sede_id)
#         return json.dumps({"datos_sede": data})

#     def consultar_cuit(self, session_id, cpu_id, sede_id):
#         # Pasar los tres parámetros a getCUIT
#         cuit = self.data_instance.getCUIT(session_id, cpu_id, sede_id)
#         return json.dumps({"cuit": cuit})

#     def generar_id_secuencia(self, session_id, cpu_id, sede_id):
#         # Pasar los tres parámetros a getSeqID
#         new_seq_id = self.data_instance.getSeqID(session_id, cpu_id, sede_id)
#         return json.dumps({"nuevo_id_secuencia": int(new_seq_id["idSeq"])})

#     def listar_logs(self, filtro="cpu"):
#         logs = self.log_instance.list()

#         if filtro == "cpu":
#             return json.dumps({"logs_por_cpu": logs}, indent=4)
#         elif filtro == "session":
#             logs_filtrados = [log for log in logs if log["sessionid"] == self.session_id]
#             return json.dumps({"logs_por_sesion": logs_filtrados}, indent=4)
#         else:
#             return json.dumps({"error": "Filtro no válido. Use 'cpu' o 'session'."})

#     # Método para listar todos los datos de CorporateData para un id_sede
#     def listar_corporate_data(self, sede_id):
#         # Obtenemos los datos para el id_sede
#         data = self.data_instance.list(sede_id)
#         return json.dumps({"datos_sede": data}, indent=4)