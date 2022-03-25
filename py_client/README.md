# conjur-api
This is an API definition for CyberArk Conjur Open Source. You can find out more at [Conjur.org](https://www.conjur.org/).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.3.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import conjur
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import conjur
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import conjur
from conjur.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = conjur.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = conjur.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with conjur.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conjur.AuthenticationApi(api_client)
    account = 'account_example' # str | Organization account name
body = 'body_example' # str | New password
x_request_id = 'test-id' # str | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  (optional)

    try:
        # Changes a user’s password.
        api_instance.change_password(account, body, x_request_id=x_request_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->change_password: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**change_password**](docs/AuthenticationApi.md#change_password) | **PUT** /authn/{account}/password | Changes a user’s password.
*AuthenticationApi* | [**enable_authenticator**](docs/AuthenticationApi.md#enable_authenticator) | **PATCH** /{authenticator}/{account} | Enables or disables authenticator defined without service_id.
*AuthenticationApi* | [**enable_authenticator_instance**](docs/AuthenticationApi.md#enable_authenticator_instance) | **PATCH** /{authenticator}/{service_id}/{account} | Enables or disables authenticator service instances.
*AuthenticationApi* | [**get_access_token**](docs/AuthenticationApi.md#get_access_token) | **POST** /authn/{account}/{login}/authenticate | Gets a short-lived access token, which is required in the header of most subsequent API requests. 
*AuthenticationApi* | [**get_access_token_via_aws**](docs/AuthenticationApi.md#get_access_token_via_aws) | **POST** /authn-iam/{service_id}/{account}/{login}/authenticate | Get a short-lived access token for applications running in AWS.
*AuthenticationApi* | [**get_access_token_via_azure**](docs/AuthenticationApi.md#get_access_token_via_azure) | **POST** /authn-azure/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Azure.
*AuthenticationApi* | [**get_access_token_via_gcp**](docs/AuthenticationApi.md#get_access_token_via_gcp) | **POST** /authn-gcp/{account}/authenticate | Gets a short-lived access token for applications running in Google Cloud Platform. 
*AuthenticationApi* | [**get_access_token_via_jwt**](docs/AuthenticationApi.md#get_access_token_via_jwt) | **POST** /authn-jwt/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. 
*AuthenticationApi* | [**get_access_token_via_jwt_with_id**](docs/AuthenticationApi.md#get_access_token_via_jwt_with_id) | **POST** /authn-jwt/{service_id}/{account}/{id}/authenticate | Gets a short-lived access token for applications using JSON Web Token (JWT) to access the Conjur API. Covers the case of use of optional URL parameter \&quot;ID\&quot; 
*AuthenticationApi* | [**get_access_token_via_kubernetes**](docs/AuthenticationApi.md#get_access_token_via_kubernetes) | **POST** /authn-k8s/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for applications running in Kubernetes.
*AuthenticationApi* | [**get_access_token_via_ldap**](docs/AuthenticationApi.md#get_access_token_via_ldap) | **POST** /authn-ldap/{service_id}/{account}/{login}/authenticate | Gets a short-lived access token for users and hosts using their LDAP identity to access the Conjur API. 
*AuthenticationApi* | [**get_access_token_via_oidc**](docs/AuthenticationApi.md#get_access_token_via_oidc) | **POST** /authn-oidc/{service_id}/{account}/authenticate | Gets a short-lived access token for applications using OpenID Connect (OIDC) to access the Conjur API. 
*AuthenticationApi* | [**get_api_key**](docs/AuthenticationApi.md#get_api_key) | **GET** /authn/{account}/login | Gets the API key of a user given the username and password via HTTP Basic Authentication. 
*AuthenticationApi* | [**get_api_key_via_ldap**](docs/AuthenticationApi.md#get_api_key_via_ldap) | **GET** /authn-ldap/{service_id}/{account}/login | Gets the Conjur API key of a user given the LDAP username and password via HTTP Basic Authentication. 
*AuthenticationApi* | [**k8s_inject_client_cert**](docs/AuthenticationApi.md#k8s_inject_client_cert) | **POST** /authn-k8s/{service_id}/inject_client_cert | For applications running in Kubernetes; sends Conjur a certificate signing request (CSR) and requests a client certificate injected into the application&#39;s Kubernetes pod. 
*AuthenticationApi* | [**rotate_api_key**](docs/AuthenticationApi.md#rotate_api_key) | **PUT** /authn/{account}/api_key | Rotates a role&#39;s API key.
*CertificateAuthorityApi* | [**sign**](docs/CertificateAuthorityApi.md#sign) | **POST** /ca/{account}/{service_id}/sign | Gets a signed certificate from the configured Certificate Authority service.
*HostFactoryApi* | [**create_host**](docs/HostFactoryApi.md#create_host) | **POST** /host_factories/hosts | Creates a Host using the Host Factory.
*HostFactoryApi* | [**create_token**](docs/HostFactoryApi.md#create_token) | **POST** /host_factory_tokens | Creates one or more host identity tokens.
*HostFactoryApi* | [**revoke_token**](docs/HostFactoryApi.md#revoke_token) | **DELETE** /host_factory_tokens/{token} | Revokes a token, immediately disabling it.
*PoliciesApi* | [**load_policy**](docs/PoliciesApi.md#load_policy) | **POST** /policies/{account}/policy/{identifier} | Adds data to the existing Conjur policy.
*PoliciesApi* | [**replace_policy**](docs/PoliciesApi.md#replace_policy) | **PUT** /policies/{account}/policy/{identifier} | Loads or replaces a Conjur policy document.
*PoliciesApi* | [**update_policy**](docs/PoliciesApi.md#update_policy) | **PATCH** /policies/{account}/policy/{identifier} | Modifies an existing Conjur policy.
*PublicKeysApi* | [**show_public_keys**](docs/PublicKeysApi.md#show_public_keys) | **GET** /public_keys/{account}/{kind}/{identifier} | Shows all public keys for a resource.
*ResourcesApi* | [**show_resource**](docs/ResourcesApi.md#show_resource) | **GET** /resources/{account}/{kind}/{identifier} | Shows a description of a single resource.
*ResourcesApi* | [**show_resources_for_account**](docs/ResourcesApi.md#show_resources_for_account) | **GET** /resources/{account} | Lists resources within an organization account.
*ResourcesApi* | [**show_resources_for_all_accounts**](docs/ResourcesApi.md#show_resources_for_all_accounts) | **GET** /resources | Lists resources within an organization account.
*ResourcesApi* | [**show_resources_for_kind**](docs/ResourcesApi.md#show_resources_for_kind) | **GET** /resources/{account}/{kind} | Lists resources of the same kind within an organization account.
*RolesApi* | [**add_member_to_role**](docs/RolesApi.md#add_member_to_role) | **POST** /roles/{account}/{kind}/{identifier} | Update or modify an existing role membership
*RolesApi* | [**remove_member_from_role**](docs/RolesApi.md#remove_member_from_role) | **DELETE** /roles/{account}/{kind}/{identifier} | Deletes an existing role membership
*RolesApi* | [**show_role**](docs/RolesApi.md#show_role) | **GET** /roles/{account}/{kind}/{identifier} | Get role information
*SecretsApi* | [**create_secret**](docs/SecretsApi.md#create_secret) | **POST** /secrets/{account}/{kind}/{identifier} | Creates a secret value within the specified variable.
*SecretsApi* | [**get_secret**](docs/SecretsApi.md#get_secret) | **GET** /secrets/{account}/{kind}/{identifier} | Fetches the value of a secret from the specified Secret.
*SecretsApi* | [**get_secrets**](docs/SecretsApi.md#get_secrets) | **GET** /secrets | Fetch multiple secrets
*StatusApi* | [**get_authenticators**](docs/StatusApi.md#get_authenticators) | **GET** /authenticators | Details about which authenticators are on the Conjur Server
*StatusApi* | [**get_gcp_authenticator_status**](docs/StatusApi.md#get_gcp_authenticator_status) | **GET** /authn-gcp/{account}/status | Details whether an authentication service has been configured properly
*StatusApi* | [**get_service_authenticator_status**](docs/StatusApi.md#get_service_authenticator_status) | **GET** /{authenticator}/{service_id}/{account}/status | Details whether an authentication service has been configured properly
*StatusApi* | [**health**](docs/StatusApi.md#health) | **GET** /health | Health info about conjur
*StatusApi* | [**info**](docs/StatusApi.md#info) | **GET** /info | Basic information about the Conjur Enterprise server
*StatusApi* | [**remote_health**](docs/StatusApi.md#remote_health) | **GET** /remote_health/{remote} | Health info about a given Conjur Enterprise server
*StatusApi* | [**who_am_i**](docs/StatusApi.md#who_am_i) | **GET** /whoami | Provides information about the client making an API request.


## Documentation For Models

 - [AuthenticatorStatus](docs/AuthenticatorStatus.md)
 - [AuthenticatorsResponse](docs/AuthenticatorsResponse.md)
 - [AzureIdentityToken](docs/AzureIdentityToken.md)
 - [CertificateJson](docs/CertificateJson.md)
 - [CreateHost](docs/CreateHost.md)
 - [CreateHostForm](docs/CreateHostForm.md)
 - [CreateHostTokenForm](docs/CreateHostTokenForm.md)
 - [CsrBody](docs/CsrBody.md)
 - [EnableAuthenticatorSetting](docs/EnableAuthenticatorSetting.md)
 - [GoogleIdentityToken](docs/GoogleIdentityToken.md)
 - [Info](docs/Info.md)
 - [InfoAuthenticators](docs/InfoAuthenticators.md)
 - [JWTToken](docs/JWTToken.md)
 - [LoadedPolicy](docs/LoadedPolicy.md)
 - [OIDCToken](docs/OIDCToken.md)
 - [PolicyVersion](docs/PolicyVersion.md)
 - [Resource](docs/Resource.md)
 - [ResourcePermissions](docs/ResourcePermissions.md)
 - [ResourceSecrets](docs/ResourceSecrets.md)
 - [ServiceAuthenticators](docs/ServiceAuthenticators.md)
 - [WhoAmI](docs/WhoAmI.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## conjurAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## conjurKubernetesMutualTls



## Author

conj_maintainers@cyberark.com

