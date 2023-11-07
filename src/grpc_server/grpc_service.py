from concurrent import futures
import grpc
from src.pb import visualization_pb2, visualization_pb2_grpc
from src.service.prompter import Prompter


class VisualizationService(visualization_pb2_grpc.VisualizationServiceServicer):

    def __init__(self, prompter: Prompter):
        self.prompter = prompter
        super().__init__()

    def ProcessImageAndPrompt(
        self, request: visualization_pb2.ImagePromptRequest,
        context: grpc.ServicerContext
    ) -> visualization_pb2.ImagePromptResponse:
        # TODO: verify JWT token # pylint: disable=fixme
        image_data = request.image_data
        prompt = request.prompt

        try:
            response_to_prompt = self.prompter.process_image_and_prompt(
                image_data=image_data, content_type="image/*", prompt=prompt
            )
            response = visualization_pb2.ImagePromptResponse(
                response_to_prompt=response_to_prompt
            )
            return response
        except Exception as exc:
            raise grpc.RpcError( # pylint: disable=raise-missing-from
                grpc.StatusCode.UNKNOWN, "An unknown error occurred."
            ) from exc


def serve(
    azure_key: str, azure_endpoint: str, openai_key: str, host: str, port: str
):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prompter = Prompter(azure_key, azure_endpoint, openai_key)
    visualization_pb2_grpc.add_VisualizationServiceServicer_to_server(
        VisualizationService(prompter), server
    )
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    server.wait_for_termination()
