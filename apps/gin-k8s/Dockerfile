FROM golang:1.12

RUN go get -u github.com/gin-gonic/gin

RUN mkdir -p /go/src/gin-k8s
ADD . /go/src/gin-k8s

WORKDIR /go/src/gin-k8s

EXPOSE 5000

ENTRYPOINT ["go", "run", "/go/src/gin-k8s/main.go"]