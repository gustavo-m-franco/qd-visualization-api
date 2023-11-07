import logging
from typing import Union
from openai import ChatCompletion
import openai

from src.service.service_error import ServiceError


class OpenIAChatCompletion(ChatCompletion):

    def __init__(self, api_key: str):
        openai.api_key = api_key

    def complete(self, prompt: str) -> Union[str, None]:
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{
                    "role": "user",
                    "content": prompt
                }],
                max_tokens=1000,
            )
            return completion.choices[0].message.content
        except openai.error.APIError as error:
            logging.error("OpenAI API returned an API Error: %s", error)
            raise ServiceError("OpenAI API returned an API Error.") from error
        except openai.error.APIConnectionError as error:
            logging.error("Failed to connect to OpenAI API: %s", error)
            raise ServiceError("Failed to connect to OpenAI API.") from error
        except openai.error.RateLimitError as error:
            logging.error("penAI API request exceeded rate limit: %s", error)
            raise ServiceError(
                "OpenAI API request exceeded rate limit."
            ) from error
        except openai.error.AuthenticationError as error:
            logging.error("Authentication OpenAI API Error: %s", error)
            raise ServiceError("Authentication OpenAI API Error.") from error
        except Exception as error:
            logging.error("OpenAI API Error: %s", error)
            raise ServiceError("OpenAI API Error.") from error
