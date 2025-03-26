'''
OpenSSL Creates TLS Server Request
'''
import subprocess
import os


def main():
    hostnames = []
    while True:
        hostname = input('Domain (press Enter to continue): ')
        if hostname == '':
            if len(hostnames) == 0:
                print('At least one domain is required!')
                continue
            break
        hostnames.append(hostname)

    new_environ = os.environ.copy()
    new_environ['SAN'] = ','.join(f'DNS:{hostname}' for hostname in hostnames)

    subprocess.check_call(['openssl', 'req', '-new', '-config', 'etc/server.conf',
                          '-out', f'certs/{hostnames[0]}.csr', '-keyout', f'certs/{hostnames[0]}.key'], env=new_environ)

    print(f'Certificate signing request at certs/{hostnames[0]}.csr')
    print(f'New private key at certs/{hostnames[0]}.key')


if __name__ == '__main__':
    main()
