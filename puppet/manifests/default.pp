Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include system-update
include python
include apache
include curl

class {'::mongodb::server':
  auth => true,
}

mongodb::db { 'devdb':
  user          => 'user1',
  password		=> 'pass1',
  roles         => ['readWrite', 'dbAdmin'],
}

python::pip { 'awscli' :
    pkgname       => 'awscli'
}

python::pip { 'eve' :
    pkgname       => 'eve'
}