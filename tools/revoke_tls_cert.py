'''
OpenSSL TLS Cert Revocation
'''
import subprocess
import sys
from pathlib import Path
from typing import Dict, List


def main():
    cert_serial_numbers: Dict[int, str] = {}
    cert_dn: Dict[int, List[str]] = {}
    with open('ca/signing-ca/db/signing-ca.db', 'r', encoding='utf-8') as handle:
        for idx, line in enumerate(handle):
            parts = line.strip().split('\t')
            # See https://pki-tutorial.readthedocs.io/en/latest/cadb.html for DB layout
            # Certificate status flag (V=valid, R=revoked, E=expired).
            # Certificate expiration date in [YY]YYMMDDHHMMSSZ format.
            # Certificate revocation date in [YY]YYMMDDHHMMSSZ[,reason] format. Empty if not revoked.
            # Certificate serial number in hex.
            # Certificate filename or literal string ‘unknown’.
            # Certificate subject DN.
            if parts[0] == 'V':
                cert_serial_numbers[idx] = parts[3]
                cert_dn[idx] = parts[5].split('/')
    for idx, dn_parts in cert_dn.items():
        print(f'    {idx}: {' '.join(dn_parts)}')
    idx_to_revoke = int(input('Index of cert to revoke: '))
    valid_crl_reasons = [
        'unspecified',
        'keyCompromise',
        'CACompromise',
        'affiliationChanged',
        'superseded',
        'cessationOfOperation',
        'certificateHold',
        'removeFromCRL'
    ]
    for idx, reason in enumerate(valid_crl_reasons):
        print(f'    {idx}: {reason}')
    revocation_reason_idx = int(input('Revocation reason index: '))

    cert = Path(f'ca/signing-ca/{cert_serial_numbers[idx_to_revoke]}.pem')
    if not cert.is_file():
        print(f'Unable to find {cert.as_posix()}')
        sys.exit(-1)

    cmd = [
        'openssl', 'ca',
        '-config', 'etc/signing-ca.conf',
        '-revoke', cert,
        '-crl_reason', valid_crl_reasons[revocation_reason_idx]
    ]
        
    subprocess.check_call(cmd)

    cmd = [
        'openssl', 'ca',
        '-gencrl',
        '-config', 'etc/signing-ca.conf',
        '-out', 'crl/signing-ca.crl'
    ]
    subprocess.check_call(cmd)



if __name__ == '__main__':
    main()
