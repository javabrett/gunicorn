import ssl

workers = 1
certfile = "../server.crt"
keyfile = "../server.key"
ssl_version = "TLSv1_2"
#ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)

if ssl.HAS_TLSv1_3:
    print("{0} with support for TLS 1.3".format(ssl.OPENSSL_VERSION))
    #ssl_context.options |= (
        #ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1 | ssl.OP_NO_TLSv1_2
    #)
else:
    print("{0} WITHOUT support for TLS 1.3, using TLS 1.2".format(ssl.OPENSSL_VERSION))
    #ssl_context.options |= (
        #ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    #)
