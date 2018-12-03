#!/usr/bin/env python3

import socket
import traceback

def get_ip()->str:
    ip_address = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 443))
        ip_address = '{}'.format(s.getsockname()[0])
        s.close()
    except:
        traceback.print_exc()
    return ip_address


if __name__ == '__main__':
    print(get_ip())

# EOF
