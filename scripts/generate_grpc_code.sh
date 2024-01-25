#!/bin/bash

cd qd-protobuf-definitions
git pull origin main
cd -
cp qd-protobuf-definitions/v1/visualization/visualization.proto pb/visualization.proto
cd pb
buf generate
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. visualization.proto

# Generated file name
FILE="visualization_pb2_grpc.py"

# Check if the file exists
if [ -f $FILE ]; then
    # Use sed to replace the line
    sed -i '' 's/^import visualization_pb2 as visualization__pb2/from . import visualization_pb2 as visualization__pb2/' "$FILE"
    echo "File modified successfully."
else
    echo "Error: '$FILE' not found."
fi

mv visualization_pb2_grpc.py ../src/pb/
mv visualization_pb2.py ../src/pb/
