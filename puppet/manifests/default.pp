Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include sysupdate
include python
include apache
include curl

class {'::mongodb::globals':
    manage_package_repo => true,
}->
class {'::mongodb::server':
  auth  => true,
  bind_ip => ['0.0.0.0'],
  verbose => true,
}->
class {'::mongodb::client': }

mongodb_user { 'admin':
  username      => 'admin',
  ensure        => present,
  password_hash => mongodb_password('admin', 'changeme!'),
  database      => 'admin',
  roles         => ['dbAdminAnyDatabase','userAdminAnyDatabase','clusterAdmin'],
  tries         => 10,
  require       => Class['mongodb::server'],
}
#mongodb_user { devdb:
#  username      => $dev,
#  ensure        => present,
#  password_hash => mongodb_password($dev, $devpass),
#  database      => 'devdb',
#  roles         => ['readWrite', 'dbAdmin'],
#  tries         => 10,
#  require       => Class['mongodb::server'],
#}

python::pip { 'awscli' :
  pkgname  => 'awscli' 
}

python::pip { 'eve' :
  pkgname => 'eve'
}
