#!/bin/bash
if mountpoint -q ./private; then
    veracrypt -u ./private
fi
if [ -d './private' ]; then
    rmdir ./private
fi