#!/bin/bash
mkdir -p ./private
if ! findmnt ./private; then
    veracrypt -m ro -t -k "" --pim=20000 --protect-hidden=no secure.hc ./private
fi