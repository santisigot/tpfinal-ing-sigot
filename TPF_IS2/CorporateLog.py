import uuid
from datetime import datetime
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import logging
from singleton import SingletonMeta

class CorporateLog(metaclass=SingletonMeta):
    def __init__(self):
        self.CPUid = str(uuid.getnode())
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateLog')

    @staticmethod
    def getInstance():
        return CorporateLog()
    
    def post(self, sessionid):
        logging.debug(f"Registrando acción en CorporateLog con session ID {sessionid}")
        try:
            uniqueID = str(uuid.uuid4())
            ts = datetime.now().isoformat()
            item = {
                'id': uniqueID,
                'CPUid': self.CPUid,
                'sessionid': sessionid,
                'timestamp': ts
            }
            response = self.table.put_item(Item=item)
            logging.debug(f"Respuesta de DynamoDB: {response}")
            return item  # Retornar los datos que se guardaron
        except Exception as e:
            logging.error(f"Error en post de CorporateLog: {e}")
            return f"Error al guardar el registro en DynamoDB: {e}"

    def list(self):
        try:
            response = self.table.scan(
                FilterExpression="CPUid = :CPUid",
                ExpressionAttributeValues={":CPUid": self.CPUid}
            )
            logs = response.get('Items', [])
            return logs if logs else "No se encontraron registros para la CPU especificada."
        except (BotoCoreError, ClientError) as error:
            return f"Error al listar los registros en DynamoDB: {error}"
