Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

include stdlib
include system-update
include python
include apache

python::pip { 'awscli' :
    pkgname       => 'awscli'
}