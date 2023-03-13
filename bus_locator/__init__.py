import logging
import azure.functions as func
from .webdata import Webdata


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        webdata = Webdata(url)
        webdata.save_to_blob()        
        return func.HttpResponse(f"URL: {url}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url in the query string or in the request body for a personalized response.",
             status_code=200
        )
