# Download latest protobuf definition
mkdir -p protobuf_definition
rm master.tar.gz
wget --no-check-certificate https://github.com/nanoapi/protobuf/archive/master.tar.gz
tar xpvf master.tar.gz

# Generate Python code
protoc --proto_path=protobuf-master --python_out=src protobuf-master/core.proto
