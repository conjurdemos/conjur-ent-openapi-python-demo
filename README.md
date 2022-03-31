# Spec-Generated Python API Client Example

This example is meant to give an example use case for OpenAPI spec generated clients.
This example is specific to Python, but generalizable to other languages.
The generated client code contains all the endpoint definitions for the Conjur APIs.
Documentation regarding format and use of OpenAPI client instances and their functions is
generated with the client, and can be found in the `docs` folder of the client library.
The documentation is formatted in markdown language. While comprehensive, it is hard
to read unless you create a repo or use other means to format the markdown.
There is also setup code that will load the client library into a Python application environment.

For this example, you will need to:
 - clone or otherwise replicate the Conjur OpenAPI spec repo at:
	https://github.com/cyberark/conjur-openapi-spec
 - create a Conjur Enterprise cluster (a leader node at minimum)

There are three steps to running the demo:
 - edit the config file
 - run the start script
 - edit/run the test python client

##0-config.sh:
You first need to edit the 0-config.sh file with:
 - the path to the OpenAPI spec repo
 - specific values for your Conjur Enterprise environment.

##1-start.sh
This script only needs be run once. It will:
 - source the config.sh file;
 - generate a Python client library named "py_client" in the current directory;
 - start a Python container that mounts the generated library and a test application;
 - load the Python client library in the application environment;
 - run 2-run_python_test_app.sh script to run the test application in the container.

##2-run_python_test_app.sh
This script runs the python application in the container. The app exercises several
API endpoints and is largely built from the code samples in the documentation. The 
app will:
- Authenticate as an admin user
- Rotate a non-admin user's API key
- Load policies
- Store and retrieve secrets
- Delete a secret

##python_app.py
The Python example application is in the bin directory and mounted in the Python
container. You can edit the app run it in the container to test it. It is meant to
provide you with a framework for experimentation.
