# Set up server configuration with puppet

file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'aplus_server
    HostName 3.86.7.178
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
