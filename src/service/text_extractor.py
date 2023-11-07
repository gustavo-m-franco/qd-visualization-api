from abc import ABC, abstractmethod
from typing import Union


class TextExtractor(ABC):

    @abstractmethod
    def extract_text_from_image_file(
        self, image_data: bytes, content_type: str
    ) -> Union[str, None]:
        pass
