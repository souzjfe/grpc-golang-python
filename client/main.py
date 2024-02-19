import grpc
import random

import number_pb2
import number_pb2_grpc

def generate_number():
    return random.randint(1, 100)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = number_pb2_grpc.NumberStub(channel)
    while True:
        number = generate_number()
        response = stub.SendNumber(number_pb2.NumberRequest(number=number))
        print("Maior número registrado até agora:", response.max_number)

if __name__ == '__main__':
    run()
