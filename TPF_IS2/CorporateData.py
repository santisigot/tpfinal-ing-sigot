import uuid
from datetime import datetime
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import logging
from singleton import SingletonMeta

class CorporateData(metaclass=SingletonMeta):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('CorporateData')

    @staticmethod
    def getInstance():
        return CorporateData()

    def getData(self, uuid_session, uuid_cpu, id):
        try:
            response = self.table.get_item(
                Key={'id': id}
            )
            data = response.get('Item', {})
            return data if data else {"error": "Datos no encontrados"}
        except (BotoCoreError, ClientError) as error:
            return {"error": f"Error al obtener datos: {error}"}

    def getCUIT(self, uuid_session, uuid_cpu, id):
        try:
            response = self.table.get_item(
                Key={'id': id}
            )
            cuit = response.get('Item', {}).get('CUIT', 'No encontrado')
            return {"CUIT": cuit}
        except (BotoCoreError, ClientError) as error:
            return {"CUIT": "No encontrado"}

    def getSeqID(self, uuid_session, uuid_cpu, id):
        try:
            response = self.table.get_item(
                Key={'id': id}
            )
            seq_id = response.get('Item', {}).get('idSeq', 'No encontrado')
            return {"idSeq": seq_id}
        except (BotoCoreError, ClientError) as error:
            return {"idSeq": "No encontrado"}

    def listCorporateData(self, id):
        try:
            response = self.table.scan()
            data = response.get('Items', [])
            return data if data else {"error": "No hay datos para la sede"}
        except (BotoCoreError, ClientError) as error:
            return {"error": f"Error al listar datos: {error}"}
