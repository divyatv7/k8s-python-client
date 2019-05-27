#Minikube Installation for mac:

###Install Homebrew:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

###Install Docker for Mac

###Install virtualbox:

brew cask install virtualbox
or
brew cask reinstall virtualbox

###Install and Run minikube

curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.27.0/minikube-darwin-amd64 &&\
      chmod +x minikube &&\
      sudo mv minikube /usr/local/bin/
minikube start

#Minikube Installation for Linux:

###Download the static binary

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube

###Add the Minikube executable to your path:

sudo cp minikube /usr/local/bin && rm minikube

minikube start




#Setup and Installation for k8s-python-client:

###From source:

git clone --recursive https://github.com/kubernetes-client/python.git
cd python
python setup.py install

###From PyPi directly:

pip install kubernetes
