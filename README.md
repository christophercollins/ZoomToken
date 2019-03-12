# ZoomToken

This python class will generate [Zoom](https://zoom.us) JWT tokens for use with v2 of the [Zoom API](https://zoom.github.io/api/#authentication) and takes care of regenerating expired tokens dynamically.

## Requirements:
The pyjwt python library is required. `pip install pyjwt`

## Usage
1. Either import the ZoomToken.py file or copy the class into your project directly.
2. Instantiate an instance of the ZoomToken class using your ZOOM API Key and Secret, and optionally, provide a `time_delta` value to set the desired life of each JWT token. (default is 60 seconds)
3. Call the `.token` attribute on your ZoomToken object whenever you need to provide a token as an argument, (e.g. when providing to the requests library during an API call) and the object will dynamically give you a new token if the previously generated one has expired.

Example:

```python
>>> from ZoomToken import ZoomToken
>>> token = ZoomToken(your_zoom_api_key, your_zoom_api_secret, time_delta=90)
>>> token.token
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJraXNzbXlidXR0IiwiZXhwIjoxNTUyNDMxMzE3fQ.1AmjK6Tv0PhL8Bqp_qWw6Hx14qyod8I4umCF9SHvpVM'
```
