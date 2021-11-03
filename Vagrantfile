Vagrant.configure("2") do |config|
  config.vm.box = 'ubuntu/xenial64'
  config.vm.hostname  = 'detoxify'
  config.vm.provider "virtualbox" do |vb|
	vb.memory=5120
    vb.name  = 'detoxify'
  end
  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/detoxify/docker-compose-dev.yml", run: "always"
end