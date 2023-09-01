#!/bin/bash
# takes a URL, send a GET request to it, and displays the body of the response
curl -sL -X "GET" $1
