## RECAST command line interface

Command Line interface used to interact with the RECAST API. For POST commands, one should provide their ORCID_ID & ACCESS_TOKEN in the `recastcli/resources/config.yaml`. 

Examples of YAML files for submission can be found in this directory `recastcli/resources`.

Examples:

List all requests:

    recast list-requests

List specific request:

    recast list-request 86199472-ff1f-6724-05f4-de6ed50e8e57

List all analyses:
 
    recast list-analyses 

List specific analysis:

    recast list-analysis 19c471ff-2514-eb44-0d82-59563cc38dab

Downlaod specific request file:

    recast-cli download-basic-request <request_id> <point_request_index> <basic_request_index> --path <optional/path/to/file.zip>

Download specific response file:

    recast-cli download-basic-response <response_id> <point_response_index> <basic_response_index> --path </optional/path/to/file.zip>
    
Upload request file:

    recast-cli upload-basic-request --request_id <id> --basic_id <id> --path </file.zip>
    
Upload response file:

    recast-cli upload-basic-response --basic_id <id> --path </responsefile.zip>
    
Create analysis:

    recast-cli add-analysis yaml-analysis-file.yaml
    
Create request:

    recast-cli add-request yaml-request-file.yaml

Request tree: (prints point request and basic request indices given a request ID)

    recast-cli request-tree <request_id>
    
Response tree: (prints point response and basic response indices given a response ID)

    recast-cli response-tree <response_id>
