'''
Signs a TLS Server request
'''
import subprocess
from pathlib import Path


def main():
    csr = Path(input('Path to Certificate Signing Request: '))
    if not csr.exists():
        print('Invalid path!')
        return
    output_path = csr.with_suffix('.crt')
    cmd = ['openssl', 'ca', '-config', 'etc/signing-ca.conf', '-in',
           csr.as_posix(), '-out', output_path.as_posix(), '-extensions',  'server_ext']
    subprocess.check_call(cmd)

    print(f'Signed Certificate at {output_path.as_posix()}')

if __name__ == '__main__':
    main()
