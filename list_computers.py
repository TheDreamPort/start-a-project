#!/usr/bin/env python
import sys
import winrm
from winrm.protocol import Protocol

ps_script = """Get-ADComputer -Filter * | Select-Object DNSHostName"""
s = winrm.Session('https://hqadc16.hq1.com:5986/wsman', auth=(sys.argv[1], sys.argv[2]), server_cert_validation='ignore' )
r = s.run_ps(ps_script)
print r.std_out