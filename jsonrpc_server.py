from jsonrpcserver import method, serve


@method
def double(x):
    return x * 2


if __name__ == '__main__':
    serve()
