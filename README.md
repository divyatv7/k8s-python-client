# Minikube Installation for mac:

### Install Homebrew:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### Install Docker for Mac

### Install virtualbox:

brew cask install virtualbox
or
brew cask reinstall virtualbox

### Install and Run minikube

curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.27.0/minikube-darwin-amd64 &&\
      chmod +x minikube &&\
      sudo mv minikube /usr/local/bin/
minikube start

# Minikube Installation for Linux:

### Download the static binary

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube

### Add the Minikube executable to your path:

sudo cp minikube /usr/local/bin && rm minikube

minikube start


# Windows Installation

### Run Command Prompt as Administrator

### Download Chocolatey

@ "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

### Install Minikube and Kubernetes cli

choco install minikube

choco intall kubernetes-cli


### Enable Hyper-V using PowerShell

Open a PowerShell console as Administrator.

### Run the following command:

Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

Reboot the system once the installation is done

### Enable Hyper-V with CMD and DISM

DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V

### Enable the Hyper-V role through Settings

Right click on the Windows button and select ‘Apps and Features’.

Select Programs and Features on the right under related settings.

Select Turn Windows Features on or off.

Select Hyper-V and click OK.


### Create a Virtual machine using HyperV

### Run Minikube

minikube start --vm-driver hyperv --hyperv-virtual-switch "Default Switch"


# Setup and Installation for k8s-python-client:

### From source:

git clone --recursive https://github.com/kubernetes-client/python.git

cd python

python setup.py install

### From PyPi directly:

pip install kubernetes
