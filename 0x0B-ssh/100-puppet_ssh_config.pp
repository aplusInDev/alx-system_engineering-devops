# Set up server configuration with puppet

file_line{'Set alias name':
  path => '/etc/ssh/ssh_config_v2',
  line => 'web-01
    HostName 100.25.20.254
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
