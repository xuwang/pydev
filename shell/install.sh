#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc
apt-get update -q
sudo apt-get install -q -y git
sudo apt-get install -q -y ruby-dev
gem install librarian-puppet
cd /vagrant/puppet && librarian-puppet install --path=/vagrant/puppet/modules
sudo mkdir -p /etc/puppet && touch /etc/puppet/hiera.yaml
