[![Build Status](https://travis-ci.org/dincho/ansible-remote-syslog.svg?branch=master)](https://travis-ci.org/dincho/ansible-remote-syslog)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-published-blue.svg)](https://galaxy.ansible.com/detail#/role/6270)

Remote Syslog
=========

Set up a [papertrail remote syslog](https://github.com/papertrail/remote_syslog2) on Debian-like systems.

Requirements
------------

none

Role Variables
--------------

* `remote_syslog_version`: [default: `v0.15`]: Version to install (see [releases](https://github.com/papertrail/remote_syslog2/releases))
* `remote_syslog_host`: [default: undefined]: Syslog host (**required**)
* `remote_syslog_port`: [default: undefined]: Syslog port (**required**)
* `remote_syslog_protocol`: [default: `tls`]: Transport protocol (tcp/tls/udp)
* `remote_syslog_files`: [default: empty]: List of files to monitor and send to remote syslog

Dependencies
------------

None

Example Playbook
----------------
    - hosts: servers
      vars:
        remote_syslog_host: logs.papertrailapp.com
        remote_syslog_port: 1234
        remote_syslog_files:
          - /var/log/php5-fpm.log
          - /var/log/nginx/error.log
          - /var/log/nginx/*.error_log
          - /var/log/mysql/error.log
      roles:
         - dincho.remote-syslog

License
-------

MIT
