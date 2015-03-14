# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #config.vm.box = "precise64"
  #config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.box = "trusty64"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
  config.vm.network :private_network, ip: "192.168.33.101"
  #mongo
  # config.vm.network "forwarded_port", guest: 27017, host: 27017, auto_correct: true
  # config.vm.network "forwarded_port", guest: 28017, host: 28017, auto_correct: true
  # web
  # config.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correct: true
  # config.vm.network "forwarded_port", guest: 443, host: 443, auto_correct: true
  # config.vm.network "forwarded_port", guest: 80, host: 80, auto_correct: true

  config.vm.synced_folder "./", "/vagrant"
  
  config.vm.provision :shell, :path => "shell/install.sh"
  config.vm.provision :shell, :path => "shell/facts.sh"
  
  config.vm.provision "puppet" do |puppet|
    puppet.temp_dir = "/tmp"
    puppet.manifests_path = "puppet/manifests"
    puppet.module_path = "puppet/modules"
    puppet.options = ['--verbose']
  end
end
