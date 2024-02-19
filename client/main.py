import grpc
import time
import random
from math_pb2_grpc import MathStub
from math_pb2 import Request, Response
def main():
    channel = grpc.insecure_channel('localhost:50005')
    stub = MathStub(channel)

    def generate_requests():
        while True:
            num = random.randint(0, 100)
            print("new number {} sent".format(num))
            yield Request(num=num, name="client")
            time.sleep(0.2)

    responses = stub.Max(generate_requests())

    for response in responses:
        print("new max {} received".format(response.result))
        print("name {} received".format(response.name))

if __name__ == '__main__':
    main()
