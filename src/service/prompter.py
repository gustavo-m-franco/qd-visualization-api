from typing import Union

from src.service.azure_text_extractor import AzureComputerVisionTextExtractor
from src.service.openai_chat_completion import OpenIAChatCompletion


class Prompter:

    def __init__(self, azure_key: str, azure_endpoint: str, openai_key: str):
        self.azure_text_extractor = AzureComputerVisionTextExtractor(
            azure_key, azure_endpoint
        )
        self.chat_completion = OpenIAChatCompletion(openai_key)

    def process_image_and_prompt(
        self, image_data: bytes, content_type: str, prompt: str
    ) -> Union[str, None]:
        image_text = self.azure_text_extractor.extract_text_from_image_file(
            image_data, content_type
        )

        full_prompt = f"{image_text}\n\n\n\n\n\n\n{prompt}"
        response = self.chat_completion.complete(full_prompt)

        return response
