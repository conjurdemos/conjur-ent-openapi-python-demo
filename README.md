# Spec-Generated Python API Client Example

This example is meant to give an example use case for OpenAPI spec generated clients.
It covers using some of the most popular Conjur Enterprise endpoints with Python:
- Authenticate an admin user
- Rotate a user's API key
- Load policies
- Store and retrieve a secret
- Delete a secret

The `start` script is responsible for executing the example by:
- Generating a new Python client library from the OpenAPI spec
- Running the demo client script in a Python Docker container

Documentation regarding format and use of OpenAPI client instances and their functions is
generated with the client, and can be found in the `docs` folder of the client library.
