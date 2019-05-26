"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import time
import logging

import grpc

import greeter_pb2 as pb
import greeter_pb2_grpc as pbg

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(pbg.GreeterServicer):

    def SayHello(self, request, context):
        print('[SayHello] Received: {}'.format(request.name))
        return pb.HelloReply(message='Hello, %s!' % request.name)
    
    def SayHelloAgain(self, request, context):
        print('[SayHelloAgain] Received: {}'.format(request.name))
        return pb.HelloReply(message='Hello, %s again!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pbg.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()