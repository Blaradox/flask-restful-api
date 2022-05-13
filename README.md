# flask-restful-api

A test framework for using flask as a web application to receive and handle POST requests

This server has one endpoint `/test` that accepts a POST request, with one argument `"string_to_cut"`. It will return a JSON object with the key `"return_string"` and a string containing every third letter from the original string.

For example if you POST `{"string_to_cut": "evEryThiRdcHarActEr"}` it will return `{"return_string": "ETRH"}`. To test this server you can run the below `curl` command in a MacOS/Linux terminal or for a Windows system you can use WSL or git bash.

```bash
$ curl -X POST localhost:5000/test --data '{"string_to_cut": "evEryThiRdcHarActEr"}' -H 'Content-Type: application/json'
```
You should receive the below response.
```bash
{"return_string": "ETRHAE"}.
```
