# Security API

API to secure websites from malicious inputs

## Usage

Base link - https://smartsamurai-test-1.azurewebsites.net/

Construct a post request using the link and different parameters

### Relative links to which requests can be sent

- escape
  - **Available Params**
    - string ==> Input string/query you want escaped
    - type ==> Type of Input given. Currently supports: mysql, url, html
  - **Example usage in python 3.7**
    - response = requests.post("<https://smartsamurai-test-1.azurewebsites.net/escape>", json={"string" : string, "type" : type_}, auth=('user', 'pass'))
  - returns a json response with the output under "response".
- whitelist
  - **Available Params**
    - string ==> Input string to validate
    - whitelist ==> List of queries to check against
  - **Example usage in python 3.7**
    - response = requests.post("<https://smartsamurai-test-1.azurewebsites.net/whitelist>", json={"string" : string, "whitelist" : whitelist}, auth=('user', 'pass'))
  - returns a json response with the output under "response".



