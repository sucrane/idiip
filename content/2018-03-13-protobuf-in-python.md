Title: Protobuf in Python
Date: 2018-03-13

[Protobuf](https://en.wikipedia.org/wiki/Protocol_Buffers) is a method to serializing structured objects. It helps to develop applications which are communicating with each other over a wire. `protoc` is the code generator by reading the `.proto` files and it provides Python support.

First, we will need to install the Protocol Buffers compiler `protoc`. In macOS, it is easy to install using `brew`:

```bash
$ brew install protobuf
```

Then we can use `protoc` command to generate language bindings, e.g., Python:

```bash
$ protoc --python_out=/path/to/your/dest/directory your.proto
```

And install `protobuf` runtime in Python using `pip`:

```bash
$ pip install protobuf
```

Make sure the runtime version is the same as `protoc` binary, or it may not work.