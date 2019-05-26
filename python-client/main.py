"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import greeter_pb2 as pb
import greeter_pb2_grpc as pbg


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pbg.GreeterStub(channel)
        hello_request = pb.HelloRequest(name='you')
        response = stub.SayHello(hello_request)
        response = stub.SayHelloAgain(hello_request)
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()