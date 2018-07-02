# Get the latest protobuf definition
#rm master.tar.gz
#wget --quiet --no-check-certificate https://github.com/nanoapi/protobuf/archive/master.tar.gz
#tar xpvf master.tar.gz
mkdir -p protobuf-master/google/protobuf
wget --quiet --no-check-certificate https://raw.githubusercontent.com/cryptocode/raiblocks/c-api/protobuf/core.proto -O protobuf-master/core.proto
wget --quiet --no-check-certificate https://raw.githubusercontent.com/cryptocode/raiblocks/c-api/protobuf/accounts.proto -O protobuf-master/accounts.proto
wget --quiet --no-check-certificate https://raw.githubusercontent.com/cryptocode/raiblocks/c-api/protobuf/util.proto -O protobuf-master/util.proto
wget --quiet --no-check-certificate https://raw.githubusercontent.com/cryptocode/raiblocks/c-api/protobuf/google/protobuf/wrappers.proto -O protobuf-master/google/protobuf/wrappers.proto

# Generate Python code
protoc --proto_path=protobuf-master --python_out=src protobuf-master/core.proto
protoc --proto_path=protobuf-master --python_out=src protobuf-master/accounts.proto
protoc --proto_path=protobuf-master --python_out=src protobuf-master/util.proto
