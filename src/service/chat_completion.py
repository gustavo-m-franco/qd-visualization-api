from abc import ABC, abstractmethod
from typing import Union


class ChatCompletion(ABC):

    @abstractmethod
    def complete(self, prompt: str) -> Union[str, None]:
        pass
