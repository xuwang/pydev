Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include sysupdate
include python
include apache
include curl

python::pip { 'awscli' :
  pkgname  => 'awscli' 
}

python::pip { 'eve' :
  pkgname => 'eve'
}

python::pip { 'flask-bootstrap' :
  pkgname => 'flask-bootstrap'
}

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
  username      => $mongo_admin,
  ensure        => present,
  password_hash => mongodb_password($mongo_admin, $mongo_admin_pass),
  database      => 'admin',
  roles         => ['readWriteAnyDatabase', 'dbAdminAnyDatabase', 'userAdminAnyDatabase', 'clusterAdmin'],
  tries         => 10,
  require       => Class['mongodb::server'],
}