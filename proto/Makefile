protocgo:
	protoc --go_out=../ --go-grpc_out=../ number.proto
protocpy:
	python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client number.proto
protoc:
	@echo "Generating Go files"
	protoc --go_out=.. --go-grpc_out=. \
		--go-grpc_opt=paths=source_relative --go_opt=paths=source_relative *.proto