#!/bin/bash
openssl req -new -config etc/signing-ca.conf -out ca/signing-ca.csr -keyout private/signing-ca.key
openssl ca -config etc/root-ca.conf -in ca/signing-ca.csr -out ca/signing-ca.crt -extensions signing_ca_ext
openssl ca -gencrl -config etc/signing-ca.conf -out crl/signing-ca.crl