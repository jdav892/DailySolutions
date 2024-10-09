def ip_to_int32(ip):
    oct = ip.split('.')
    oct1, oct2, oct3, oct4 = map(int, oct)
    return (oct1 << 24) | (oct2 << 16) | (oct3 << 8) | (oct4)