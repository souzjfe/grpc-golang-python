package main

import (
	"context"
	"log"
	"net"

	pb "buffers/number" // Substitua pelo caminho real para suas definições protobuf

	"google.golang.org/grpc"
)

type server struct {
	maxNumber int32
}

func (s *server) SendNumber(ctx context.Context, in *pb.NumberRequest) (*pb.MaxNumberResponse, error) {
	if in.Number > s.maxNumber {
		s.maxNumber = in.Number
	}
	return &pb.MaxNumberResponse{MaxNumber: s.maxNumber}, nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterNumberServer(s, &server{maxNumber: 0})
	log.Println("Server started at :50051")
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
