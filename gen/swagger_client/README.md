# REST-API client example code in .NET6

This is a simple example of a REST-API client developed in python, users can use this code as a boilerplate to integrate with Ayyeka's FAI platform, example code only works with version 2.0 of REST-API.

When running the code the following steps will be executed:
1. Authentication using a specified API Key, Secret in order to acquire an access token.
2. Fetch and print out metadata (sites, samples).
3. A loop that fetches new samples from the FAI Rest-API every 15min.

## Prerequisites

### API Key and Secret
* Follow the instructions at [Ayyeka Developer Portal](https://developer.ayyeka.com/docs/authentication) to generate the API Key,Secret.
* Update the Program.cs with generated the API Key,Secret.

```
    API_KEY = "API-KEY-HERE";
    API_SECRET = "API-SECRET-HERE";

```
    

### Developer Environment & Tools

* We used python 3.10 with VScode.
* We used swagger-codegen to generate the API client in python.
* We used openapi3.json openapi3.0 spec file Ayyek REST-API


## How to re-generate swagger_client using swagger-codegen
1. Download the swagger-codegen jar from https://swagger.io/docs/open-source-tools/swagger-codegen/
2. Run the following commands:
        ```
        java -jar .\swagger-codegen-cli.jar generate  -i .\openapi3.json  -l python   -o  .\generated_python

        ```
