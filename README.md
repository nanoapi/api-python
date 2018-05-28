# About

This is the Python client for the Nano Node API. Both Python 2 and 3 are supported, with domain socket and TCP transports.

A REST server is also included, which supports all Node messages.

# Using the API

See `src/example-socket-client.py` for an example on how to use the API. The query objects are documented here: https://nanoapi.github.io/protobuf/index.html

# REST server

The REST server supports all Node queries automatically as the Protobuffer definition is updated. Since Protobuffer has a canonical JSON representation, the protobuf documentation linked above can be used to construct REST queries and parse responses. 

Clients should create POST requests with a JSON body for the request. GET queries will be supported in the future. The response is JSON as well.

## Running

`python rest.py`

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


# Development

## Updating generated Protobuffer files

When the protobuffer definition has changed, perform the following steps to fetch the latest version and generate a new core_pb2.py file:

```
git submodule foreach git pull origin master
./protobuf-py.sh
```
