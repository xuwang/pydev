Vagrant.configure("2") do |config|
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.network :private_network, ip: "192.168.33.101"
    config.vm.synced_folder "./", "/vagrant"
	
	config.vm.provision :puppet do |puppet|
	    puppet.manifests_path = "puppet/manifests"
		puppet.module_path = "puppet/modules"
	    puppet.options = ['--verbose']
	end
	
end