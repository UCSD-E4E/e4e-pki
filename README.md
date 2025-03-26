# e4e-pki

## SSL/TLS Certificate
1. On the host server with the following attributes:

- DNS name www.example.com

Follow https://pki-tutorial.readthedocs.io/en/latest/advanced/index.html#operate-tls-ca to run the TLS server CA

# Getting Started
1. Install Veracrypt (https://www.veracrypt.fr/en/Downloads.html)
2. Mount the veracrypt volume
```
veracrypt -m ro -t -k "" --pim=20000 --protect-hidden=no secure.hc ./private
```
Note that this process will take about a minute or so.

# Getting a TLS Cert
1. Clone this repo onto the target machine
2. Run `python tools/create_tls_server_request.py` and follow the prompts
3. Send the resulting `.csr` file to the CA admin

# Operating the TLS CA
1. Copy the `.csr` file to somewhere reasonable.
2. Mount the veracrypt volume using `./tools/00_mount_crypt.sh`.
3. Sign the cert using `python tools/sign_tls_server_request.py`.
4. Commit the changes, which should only be the new cert in `certs`, a copy in `ca/signing-ca`, and a new row in `ca/signing-ca/db/signing-ca.db`.
5. Push the changes and merge.