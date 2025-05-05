'''
OpenSSL Creates TLS Client Request
'''
import subprocess
import os


def main():
    cert_name = None
    while cert_name is None or cert_name == '':
        cert_name = input('Cert file name: ')
        if cert_name == '':
            print('Cert file name is required!')
            continue

    subprocess.check_call(['openssl', 'req', '-new', '-config', 'etc/tls-client.conf',
                          '-out', f'certs/{cert_name}.csr', '-keyout', f'certs/{cert_name}.key'])

    print(f'Certificate signing request at certs/{cert_name}.csr')
    print(f'New private key at certs/{cert_name}.key')


if __name__ == '__main__':
    main()
