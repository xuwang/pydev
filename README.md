A Vagrant box for development python based applications.

The box uses Vagrant Puppet provisioner to manage configurations. 

It has following components installed:

	* Curl
	* Python
	* Docopt
	* Flask
	* Eve and Eve-doc: Python RESTful API Framework
	* AWSCLI and botocore
	* MongoDB
	* Apache2

To install Eve-doc git submodule:
	cd pydev
	git submodule update --init --recursive

