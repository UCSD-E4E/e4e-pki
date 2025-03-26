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