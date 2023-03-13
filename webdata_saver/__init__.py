import logging
import os
import requests
import azure.functions as func
from datetime import datetime
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    content = requests.get(req.params.get('url')).content
    filename = f"vehicles_locations@{datetime.strftime(datetime.now(), '%Y-%m-%d@%H-%M-%S')}.csv"
    
    blob_service_client = BlobServiceClient.from_connection_string(os.environ["STORAGE_CONNECTION_STRING"])        
    blob_client = blob_service_client.get_blob_client(container=os.environ["STORAGE_CONTAINER_NAME"], blob=filename)    
    blob_client.upload_blob(content)
    return func.HttpResponse("File saved.")