# About

This is the Python client for the Nano API. Both Python 2 and 3 are supported, with domain socket and TCP transports.

A REST server is also included, which supports all Node queries.

# Installation

Clone the repository and install dependencies:

```
git clone http://github.com/nanoapi/api-python
cd api-python
pip install -r requirements.txt
```

You may need to replace pip with pip3 on some Python3 installations

# Using the API

See `src/example-socket-client.py` for an example on how to use the API. The query objects are documented here: https://nanoapi.github.io/protobuf/index.html

# REST server

The REST server supports all Node queries automatically as the Protobuffer definition is updated. Since Protobuffer has a canonical JSON representation, the protobuf documentation linked above can be used to construct REST queries and parse responses.

Clients should create POST requests with a JSON body for the request. GET queries will be supported in the future. The response is JSON as well.

## Running

Start the server with

```
python src/rest.py
```

By default, the server listens on port 8080 and connects to the node over domain sockets. See the configuration section for information on how to change this.

## Testing

You can use curl or Postman to test queries on port 8080.

## Configuration

To override the default REST server settings, create a file `config.json` with the following structure:

```
{
    "port": 8080,
    "node": {
        "connection": "local:///tmp/nano"
    }
}
```

To connect to the node using tcp, use a connection string like `tcp://host:port`

## Errors

The REST server returns errors in the following format:

```
{
    "type": "ACCOUNT_PENDING",
    "error_code": 4,
    "error_message": "Bad account number",
    "error_category": "error_common"
}
```

# Development

## Updating generated Protobuffer files

When the protobuffer definition has changed, run the following command to fetch the latest version and generate a new Python source files:

```
ci/protobuf-gen.sh
```
