protocgo:
	protoc --go_out=../server --go-grpc_out=../server number.proto
protocpy:
	python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client number.proto
