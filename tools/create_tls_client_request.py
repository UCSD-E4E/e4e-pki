'''
OpenSSL Creates TLS Client Request
'''
import subprocess
import os


def main():
    hostnames = []
    while True:
        hostname = input('Cert file name: ')
        if hostname == '':
            if len(hostnames) == 0:
                print('Cert file name is required!')
                continue
            break
        hostnames.append(hostname)
        break

    subprocess.check_call(['openssl', 'req', '-new', '-config', 'etc/tls-client.conf',
                          '-out', f'certs/{hostnames[0]}.csr', '-keyout', f'certs/{hostnames[0]}.key'])

    print(f'Certificate signing request at certs/{hostnames[0]}.csr')
    print(f'New private key at certs/{hostnames[0]}.key')


if __name__ == '__main__':
    main()
