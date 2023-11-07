import sys
import os
import grpc
from src.pb import visualization_pb2, visualization_pb2_grpc

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        image_path = "/Users/GFC01/Desktop/AzureComputerVisionTextExtractor.png"
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        propmpt = "\n\n\n\nRefactor the code provided above..."

        stub = visualization_pb2_grpc.VisualizationServiceStub(channel)
        response = stub.ProcessImageAndPrompt(
            visualization_pb2.ImagePromptRequest(
                jwt_token="your_token", image_data=image_data, prompt=propmpt
            )
        )
        print(response.response_to_prompt)


if __name__ == '__main__':
    run()
