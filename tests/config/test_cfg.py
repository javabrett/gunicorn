import ssl
from ssl import SSLContext

bind = "unix:/tmp/bar/baz"
workers = 3
proc_name = "fooey"
default_proc_name = "blurgh"
certfile = "../examples/server.crt"
keyfile = "../examples/server.key"
ssl_context = SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.set_ciphers(("DHE-RSA-AES256-GCM-SHA384:"
                         "DHE-RSA-AES128-GCM-SHA256:"
                         "ECDHE-RSA-AES256-GCM-SHA384:"
                         "ECDHE-RSA-AES128-GCM-SHA256:"
                         "DHE-RSA-AES256-SHA256:"
                         "DHE-RSA-AES128-SHA256:"
                         "ECDHE-RSA-AES256-SHA384:"
                         "ECDHE-RSA-AES128-SHA256:"
                         "!aNULL:!eNULL:"
                         "!LOW:"
                         "!3DES:!MD5:!EXP:!PSK:!DSS:!RC4:!SEED:!ECDSA:!ADH:!IDEA:!3DES"))
