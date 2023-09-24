# Set up server configuration with puppet

file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'aplus_server
    HostName 34.204.81.175
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
