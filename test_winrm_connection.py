#!/usr/bin/env python
#
# this script is designed to run what ever you supply on the command line on the Domain controller
# of the HQ experiment domain. Note that it assumes the use of HTTPS for winrm. 
#
# The syntax to invoke this script is as follows:
# ./test_winrm_connection.py administrator <PASSWORD> tasklist
import sys
from winrm.protocol import Protocol

DEFAULT_TARGET = "hqadc16.hq1.com"

p = Protocol(	endpoint='https://%s:5986/wsman' % DEFAULT_TARGET,
			    transport='ntlm',
			    username=sys.argv[1],
			    password=sys.argv[2],
			    server_cert_validation='ignore' )

shell_id                      = p.open_shell()
command_id                    = p.run_command(shell_id, sys.argv[3], sys.argv[4:])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)
print std_out