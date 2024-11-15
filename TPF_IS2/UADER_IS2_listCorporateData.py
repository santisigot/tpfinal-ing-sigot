import boto3
import json
from decimal import Decimal
import uuid
from InterfazParaAWS import InterfazParaAWS

# Retorna una estructura JSON con todos los campos de la tabla
# CorporateData

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)  # O usa int(obj) si todos los valores son enteros
    raise TypeError

def listar_corporate_data():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CorporateData')
    
    uuid_session = str(uuid.uuid4()) 
    uuid_cpu = str(uuid.getnode()) 
    interfaz = InterfazParaAWS(uuid_session, uuid_cpu) 
    
    action = "Consulta de datos de sede"
    status = "Éxito"
    print("Registrando acción en CorporateLog...")
    
    print(interfaz.registrar_log())
    
    try:
        response = table.scan()  # Scan a todos los elementos de la tabla
        data = response.get('Items', [])
        
        # Convierte todos los elementos en 'data' utilizando la función decimal_default
        return json.dumps({"corporate_data": data}, indent=4, default=decimal_default)
    except Exception as e:
        return json.dumps({"error": f"Error al acceder a la base de datos: {e}"})

if __name__ == "__main__":
    print(listar_corporate_data())