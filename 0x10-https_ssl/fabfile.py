#!/usr/bin/python3

from fabric.api import env, get

env.hosts = ['54.236.33.138']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def get_haproxyCfg():
    get('/etc/haproxy/haproxy.cfg', '1-haproxy_ssl_termination')
