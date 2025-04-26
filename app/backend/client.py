from loguru import logger 

class BackendClient:
    """
    Template of the Backend Client
    """
    def __init__(self):
        pass
    
    def get_text1(self) -> str:
        return "Text 1"
    
    def get_text_2(self) -> str:
        return "Text 2"


def get_backend_client() -> BackendClient:
    return BackendClient()
