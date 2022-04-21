Installation
============


Python Version
--------------

Latest version of Python. Flask supports Python 3.7 and newer.


Dependencies
------------

Install required packages using: pip install -r requirements.txt



Start Server
------------

- Open command prompt
- [Optional] Activate virtual environment if set up
- Navigate to folder(verloopAssignment) with main.py
- Create .env file and add ```API_KEY="Your Google Api key"```
- Execute command: python main.py
- Use api testing tool to make request on ```http://<address>/getAddressDetails```

# Example Request:

Request type | POST

Endpoint | /getAddressDetails

Parameters:
- address: type string
- output_format: type string, valid options = ["json", "xml"]

Example json:
- Request
    ```
    {        
        "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
        "output_format": "json"
    }
    ```
- Response
    ```
    {
        "address": "3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru, Karnataka 560008, India",
        "coordinates": {
            "lat": 12.9658286,
            "lng": 77.63948169999999
        }
    }
    ```
Example xml:

- Request
    ```
    {        
        "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
        "output_format": "json"
    }
    ```
- Response
    ```
    <?xml version='1.0' encoding='UTF-8'?>
    <root>
        <address>3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru, Karnataka
        560008, India</address>
        <coordinates>
            <lat>12.9658286</lat>
            <lng>77.63948169999999</lng>
        </coordinates>
    </root>
    ```
