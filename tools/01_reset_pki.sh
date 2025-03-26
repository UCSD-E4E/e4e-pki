#!/bin/bash
# Reset root-ca database
cp /dev/null ca/root-ca/db/root-ca.db
echo 01 > ca/root-ca/db/root-ca.crt.srl
echo 01 > ca/root-ca/db/root-ca.crl.srl
rm ca/root-ca/*.pem

# Reset signing-ca database
cp /dev/null ca/signing-ca/db/signing-ca.db
echo 01 > ca/signing-ca/db/signing-ca.crt.srl
echo 01 > ca/signing-ca/db/signing-ca.crl.srl
rm ca/signing-ca/*.pem

# Nuke existing certs
rm ca/*.crt
rm certs/*.crt
rm certs/*.csr
rm certs/*.key
rm private/*.key