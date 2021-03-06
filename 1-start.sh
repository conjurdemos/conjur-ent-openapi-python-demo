#!/bin/bash

source ./0-config.sh

# Main function
main() {
  generate_python_client_library	# only needs to run once
  start_python_test_client		# only needs to run once
  ./2-run_python_test_app.sh
}

##############################################################################
# You should not need to edit anything below to run the demo.
# But of course, once you have run it successfully, feel free to modify.
##############################################################################

#======================================================
function generate_python_client_library() {

  # Generated client directory on host
  API_DIR=${PWD}/py_client

  pushd $GEN_DIR
    ./bin/generate_client -e -l python -o $API_DIR
  popd
}

#======================================================
function start_python_test_client() {

  docker stop py_test 		# remove existing test client

  # Mount point in client container for scripts and starting directory
  WORKDIR=/test/

  docker run -d --rm						\
  -e "DEBUG=False"						\
  --name py_test						\
  -v ${API_DIR}:${WORKDIR}py_client				\
  -v ${PWD}/bin/init_python.sh:${WORKDIR}init_python.sh		\
  -v ${PWD}/bin/python_app.py:${WORKDIR}python_app.py		\
  -v ${PWD}/policy:${WORKDIR}/policy				\
  -v "${CONJUR_CERT}:${WORKDIR}conjur-cert.pem"			\
  -e "CONJUR_APPLIANCE_HOSTNAME=${CONJUR_APPLIANCE_HOSTNAME}"	\
  -e "CONJUR_ACCOUNT=${CONJUR_ACCOUNT}"				\
  -e "CONJUR_AUTHN_LOGIN=${CONJUR_AUTHN_LOGIN}"			\
  -e "CONJUR_AUTHN_API_KEY=${CONJUR_AUTHN_API_KEY}"		\
  --workdir ${WORKDIR}						\
  --add-host "${CONJUR_APPLIANCE_HOSTNAME}:${CONJUR_HOST_IP_ADDRESS}"	\
  python:3							\
  bash -c "sleep infinity"

  echo "Loading Conjur Python client library..."
  docker exec py_test ./init_python.sh
}

main "$@"
