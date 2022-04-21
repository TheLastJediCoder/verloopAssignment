import json
import os
from flask import Flask, request
import requests
import urllib.parse
from xml.etree.ElementTree import Element, SubElement, tostring
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/getAddressDetails", methods=['POST'])
def getAddressDetailsV1():
    # get request details into address_details
    # Sample Request
    # {
    #     "address": "Street, City, State, Country",
    #     "output_format": "json"
    # }
    try:
        address_details = json.loads(request.data)
    except:
        error_code = {
            "error_message": "Invalid json message received",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Set address from address_details into api_address
    # Verify api_address -> Not NULL
    try:
        api_address = address_details['address'].strip()
        if api_address == "":
            error_code = {
                "error_message": "Invalid request. Missing the 'address' parameter.",
                "status": "INVALID_REQUEST"
            }
            return error_code
    except:
        error_code = {
            "error_message": "Invalid request. Missing the 'address' parameter.",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Set output format from address_details into api_output_format
    # Verify api_output_format type -> json or xml
    try:
        api_output_format = address_details['output_format']
        if api_output_format not in ['json', 'xml']:
            error_code = {
                "error_message": "Invalid request. 'output_format' parameter should be json or xml.",
                "status": "INVALID_REQUEST"
            }
            return error_code
    except:
        error_code = {
            "error_message": "Invalid request. Missing the 'output_format' parameter.",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Create url for requesting google apis
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # encode api_address
    url += f'?address={urllib.parse.quote(api_address)}'

    # set api key
    url += f'&key={os.getenv("API_KEY")}'

    # Set response from google into result
    result = requests.get(url).json()

    # Check status
    if result["status"] == 'OK':
        # converting output based on api_output_format
        if api_output_format == 'json':
            success_code = {
                "coordinates": result["results"][0]["geometry"]["location"],
                "address": result["results"][0]["formatted_address"]
            }
        elif api_output_format == 'xml':
            root = Element('root')
            address = SubElement(root, "address")
            address.text = str(result["results"][0]["formatted_address"])
            coordinates = SubElement(root, "coordinates")
            lat = SubElement(coordinates, "lat")
            lat.text = str(result["results"][0]["geometry"]["location"]['lat'])
            lng = SubElement(coordinates, "lng")
            lng.text = str(result["results"][0]["geometry"]["location"]['lng'])
            success_code = tostring(root, xml_declaration=True, encoding='UTF-8')
        return success_code
    elif result["status"] == 'ZERO_RESULTS':
        error_code = {
            "error_message": 'No result for given address',
            "address": api_address,
            "status": result['status']
        }
        return error_code

    error_code = {
        "error_message": result['error_message'] if result['error_message'] else 'Unable to process request',
        "status": result['status'] if result['status'] else 'REQUEST_FAILED'
    }
    return error_code


@app.route("/api/v2/getAddressDetails", methods=['POST'])
def getAddressDetailsV2():
    # get request details into address_details
    # Sample Request
    # {
    #     "address": "Street, City, State, Country",
    #     "output_format": "json"
    #     "api_key": "your api key"
    # }
    try:
        address_details = json.loads(request.data)
    except:
        error_code = {
            "error_message": "Invalid json message received",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Set address from address_details into api_address
    # Verify api_address -> Not NULL
    try:
        api_address = address_details['address'].strip()
        if api_address == "":
            error_code = {
                "error_message": "Invalid request. Missing the 'address' parameter.",
                "status": "INVALID_REQUEST"
            }
            return error_code
    except:
        error_code = {
            "error_message": "Invalid request. Missing the 'address' parameter.",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Set output format from address_details into api_output_format
    # Verify api_output_format type -> json or xml
    try:
        api_output_format = address_details['output_format']
        if api_output_format not in ['json', 'xml']:
            error_code = {
                "error_message": "Invalid request. 'output_format' parameter should be json or xml.",
                "status": "INVALID_REQUEST"
            }
            return error_code
    except:
        error_code = {
            "error_message": "Invalid request. Missing the 'output_format' parameter.",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Set output format from address_details into api_output_format
    # Verify api_output_format type -> json or xml
    try:
        api_key = address_details['api_key']
    except:
        error_code = {
            "error_message": "Invalid request. Missing the 'api_key' parameter.",
            "status": "INVALID_REQUEST"
        }
        return error_code

    # Create url for requesting google apis
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    # encode api_address
    url += f'?address={urllib.parse.quote(api_address)}'

    # set api key
    url += f'&key={api_key}'

    # Set response from google into result
    result = requests.get(url).json()

    # Check status
    if result["status"] == 'OK':
        # converting output based on api_output_format
        if api_output_format == 'json':
            success_code = {
                "coordinates": result["results"][0]["geometry"]["location"],
                "address": result["results"][0]["formatted_address"]
            }
        elif api_output_format == 'xml':
            root = Element('root')
            address = SubElement(root, "address")
            address.text = str(result["results"][0]["formatted_address"])
            coordinates = SubElement(root, "coordinates")
            lat = SubElement(coordinates, "lat")
            lat.text = str(result["results"][0]["geometry"]["location"]['lat'])
            lng = SubElement(coordinates, "lng")
            lng.text = str(result["results"][0]["geometry"]["location"]['lng'])
            success_code = tostring(root, xml_declaration=True, encoding='UTF-8')
        return success_code
    elif result["status"] == 'ZERO_RESULTS':
        error_code = {
            "error_message": 'No result for given address',
            "address": api_address,
            "status": result['status']
        }
        return error_code

    error_code = {
        "error_message": result['error_message'] if result['error_message'] else 'Unable to process request',
        "status": result['status'] if result['status'] else 'REQUEST_FAILED'
    }
    return error_code


if __name__ == '__main__':
    app.run(debug=False)
