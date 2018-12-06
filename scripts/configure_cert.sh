#!/bin/sh
openssl req -newkey rsa:4096 -keyform PEM -keyout winrm-admin.key.enc -out winrm-admin.csr -outform PEM