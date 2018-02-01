# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'etc'

provision = <<SCRIPT
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -y upgrade
apt install -y python3-pip vim tig git
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
apt-get install -y haveged opensc-pkcs11 yubico-piv-tool
apt-get update
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository \
 "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
 $(lsb_release -cs) \
 stable"
apt-get update
apt-get install -y docker-ce

# Add vagrant to the docker group so we don't have to type
# sudo every time.
adduser vagrant docker

cd /vagrant
cp dev/vim.conf /root/.vimrc
sudo -u vagrant cp dev/vim.conf /home/vagrant/.vimrc

pip3 install -r requirements-dev.txt
cd /vagrant
sudo -u vagrant git config user.name "$GIT_COMMITTER_NAME"
sudo -u vagrant git config user.email "$GIT_COMMITTER_EMAIL"
SCRIPT
# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.ssh.forward_agent = true

  config.vm.define "aioschedule" do |aioschedule|
    aioschedule.vm.box = "bento/ubuntu-16.04"
    aioschedule.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
      vb.customize ['modifyvm', :id, '--usb', 'on']
      vb.customize ['usbfilter', 'add', '0', '--target', :id,
        '--name', 'SmartCard', '--vendorid', '0x1050', '--productid', '0x0407']
    end

    aioschedule.vm.provision "shell" do |shell|
      shell.inline = provision
      shell.env = {"HOST_USER" => Etc.getlogin,
        "GIT_COMMITTER_EMAIL": ENV["IBR_GIT_COMMITTER_EMAIL"],
        "GIT_COMMITTER_NAME": ENV["IBR_GIT_COMMITTER_NAME"]}
    end
  end

end

