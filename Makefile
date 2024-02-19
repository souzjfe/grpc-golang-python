
protoc: protocpy protocgo
protocpy:
	@echo "Generating Py files"
	cd proto && \
		python -m grpc_tools.protoc -I. --python_out=../client --grpc_python_out=../client math.proto
protocgo:
	@echo "Generating Go files"
	cd proto && \
		protoc --go_out=../server/protobuffers --go-grpc_out=../server/protobuffers \
			--go-grpc_opt=paths=source_relative --go_opt=paths=source_relative *.proto

runserver:
	@echo "Running server"
	cd server && go run main.go

runclient:
	@echo "Running client"
	cd client && poetry run python main.py