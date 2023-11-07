from src.configurations.config import load_config
from src.grpc_server.grpc_service import serve

config = load_config("./config")

azure_key = config.get("azure").get("computer_vision").get("key")
azure_endpoint = config.get("azure").get("computer_vision").get("endpoint")
content_type = config.get("azure").get("computer_vision").get("content_type")
openai_key = config.get("openia").get("key")
host = config.get("grpc").get("host")
port = config.get("grpc").get("port")

serve(azure_key, azure_endpoint, openai_key, host, port)
