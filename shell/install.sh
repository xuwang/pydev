#!/bin/sh
sudo apt-get install -y git
sudo apt-get install -y ruby-dev
gem install librarian-puppet
cd /vagrant/puppet && librarian-puppet install --path=/vagrant/puppet/modules
