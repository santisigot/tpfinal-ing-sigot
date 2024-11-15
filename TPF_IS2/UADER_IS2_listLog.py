import boto3
import json
import uuid
from InterfazParaAWS import InterfazParaAWS
# Inicializando el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CorporateLog')

def list_logs_by_cpu(cpu_id):
    uuid_session = str(uuid.uuid4())  # Generar un UUID para la sesión
    uuid_cpu = str(uuid.getnode()) 
    interfaz = InterfazParaAWS(uuid_session, uuid_cpu) 
    # Escaneo de la tabla
    response = table.scan()
    logs = response['Items']
    
    # Imprimir todos los logs para verificar los campos disponibles
    print("Todos los logs:")
    print(json.dumps(logs, indent=4, default=str)) 

    # Filtrando logs por CPU ID
    filtered_logs = [log for log in logs if 'CPUid' in log and log['CPUid'] == cpu_id]
    
    # Retornando resultado en formato JSON
    action = "Consulta de datos de sede"
    status = "Éxito"
    print("Registrando acción en CorporateLog...")
    
    print(interfaz.registrar_log())
    
    return filtered_logs

if __name__ == '__main__':
    cpu_id = '237901788416721' 
    logs = list_logs_by_cpu(cpu_id)
    
    
    print("Logs filtrados:")
    print(json.dumps(logs, indent=4, default=str))  