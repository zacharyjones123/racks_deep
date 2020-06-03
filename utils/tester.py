from ftplib import FTP

def ftpConnection():
    ftp = FTP(host="ftp.wheelpros.com")
    ftp.connect('ftp.wheelpros.com', 21)
    print(is_port_in_use(21))
    ftp.login("ftp.wheelpros.com|1091543", "J5PU886qN2Qmhp5U")
    print(is_port_in_use(21))
    print(ftp.retrlines('LIST'))
    lista = ftp.nlst()
    return (lista)

def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

print(ftpConnection())