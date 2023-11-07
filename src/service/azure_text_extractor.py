from typing import Union
import requests

from src.service.text_extractor import TextExtractor


class AzureComputerVisionTextExtractor(TextExtractor):

    def __init__(self, subscription_key: str, endpoint: str):
        self.subscription_key = subscription_key
        self.endpoint = endpoint

    def extract_text_from_image_file(
        self, image_data: bytes, content_type: str
    ) -> Union[str, None]:
        url = f'{self.endpoint}/computervision/imageanalysis:analyze'
        headers = {
            'Content-Type': content_type,
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }

        params = {
            'features': 'caption,read',
            'model-version': 'latest',
            'language': 'en',
            'api-version': '2023-04-01-preview'
        }

        response = requests.post(
            url, headers=headers, params=params, data=image_data
        )

        if response.status_code == 200:
            read_results = response.json().get('readResult', {}).get('content')
            return read_results

        return None
