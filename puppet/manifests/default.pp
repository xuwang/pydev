Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include system-update
include python
include apache
include curl

class {'::mongodb::server':
  # auth		=> true,
  bind_ip	=> ['0.0.0.0'],
  verbose	=> true,
}

mongodb::db { 'devdb':
  user          => 'user1',
  password		=> 'pass1',
  roles         => ['readWrite', 'dbAdmin'],
}

mongodb_user { dev:
  username      => 'dev',
  ensure        => present,
  password_hash => mongodb_password('dev', 'devpass'),
  database      => devdb,
  roles         => ['readWrite', 'dbAdmin'],
  tries         => 10,
  require       => Class['mongodb::server'],
}

python::pip { 'awscli' :
    pkgname       => 'awscli'
}

python::pip { 'eve' :
    pkgname       => 'eve'
}