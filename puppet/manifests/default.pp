Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include system-update
include python
include apache

class {'::mongodb::server':
  auth => true,
}

mongodb::db { 'testdb':
  user          => 'user1',
  password_hash => 'a15fbfca5e3a758be80ceaf42458bcd8',  # hash of "user1:mongo:pass1"
}

python::pip { 'awscli' :
    pkgname       => 'awscli'
}