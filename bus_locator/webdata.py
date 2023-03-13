import os
import requests
import logging
from datetime import datetime

from azure.storage.blob import BlobServiceClient

class Webdata:

    def __init__(self, url: str) -> None:        
        response = requests.get(url)
        self.status_code = response.status_code
        self.filename = f"bus_location@{datetime.strftime(datetime.now(), '%Y-%m-%d@%H-%M-%S')}.csv"
        logging.info(self.status_code)
        self.content = response.content        
        logging.info(type(response.content))
        logging.info("Content imported to Webdata object.")
        #TODO
        self.connection_string = os.environ["AZURE_BLOB_CONNECTION_STRING"]
        self.container_name = 'test' #os.environ["AZURE_BLOB_CONTAINER_NAME"]

    def save_to_blob(self) -> bool:        
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)        
        blob_client = blob_service_client.get_blob_client(container=self.container_name, blob=self.filename)
        blob_client.upload_blob(self.content)
        logging.info("Saving data to the blob...")
        return True