# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import math_pb2 as math__pb2


class MathStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Max = channel.stream_stream(
                '/protobuf.Math/Max',
                request_serializer=math__pb2.Request.SerializeToString,
                response_deserializer=math__pb2.Response.FromString,
                )


class MathServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Max(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Max': grpc.stream_stream_rpc_method_handler(
                    servicer.Max,
                    request_deserializer=math__pb2.Request.FromString,
                    response_serializer=math__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protobuf.Math', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Math(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Max(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/protobuf.Math/Max',
            math__pb2.Request.SerializeToString,
            math__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)