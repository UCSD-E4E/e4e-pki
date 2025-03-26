#!/bin/bash
openssl req -new -config etc/root-ca.conf -out ca/root-ca.csr -keyout private/root-ca.key
openssl ca -selfsign -config etc/root-ca.conf -in ca/root-ca.csr -out ca/root-ca.crt -extensions root_ca_ext -days 7305
openssl ca -gencrl -config etc/root-ca.conf -out crl/root-ca.crl
