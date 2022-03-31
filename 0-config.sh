# Conjur Open API spec repo directory
#   see: https://github.com/cyberark/conjur-openapi-spec
GEN_DIR=../conjur-openapi-spec-main

# Conjur service configuration variables
CONJUR_ACCOUNT=dev
CONJUR_APPLIANCE_HOSTNAME=conjur-master-minikube
CONJUR_HOST_IP_ADDRESS=192.168.59.100
CONJUR_CERT=~/Conjur/cybrsm-demos/etc/conjur-master-minikube-dev.pem
CONJUR_AUTHN_LOGIN=admin
CONJUR_AUTHN_API_KEY=$(keyring get conjur adminpwd)
