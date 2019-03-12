# Copyright 2018 Christopher Collins (https://github.com/christophercollins/).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function, unicode_literals
import jwt
from datetime import timedelta, datetime
from time import mktime, time


class ZoomToken:
    """
    A class used to generate Zoom JWT tokens.

    """

    def __init__(self, api_key, api_secret, time_delta=60):
        """

        :param api_key: Your Zoom API Key
        :param api_secret: Your Zoom API Secret
        :param time_delta: Time in seconds for JWT token to be valid. Default is 60.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.time_delta = time_delta
        self.token_generated = None
        self.token_expiration = self.get_time()
        self.token_value = self.generate_token()

    def generate_timestamp(self):
        dt = datetime.now()
        future = dt + timedelta(seconds=self.time_delta)
        expiration = int(mktime(future.timetuple()))
        self.token_expiration = expiration

    @property
    def token(self):
        """
        This property returns a JWT token for Zoom.

        :return: JWT token for Zoom.
        """
        # Check if time stamp of current token is close to expiring before generating a new one
        if (self.get_time() - self.token_generated) > (self.time_delta - 10):
            self.token_value = self.generate_token()
            return self.token_value
        else:
            return self.token_value

    @staticmethod
    def get_time():
        return int(round(time()))

    def generate_token(self):
        self.generate_timestamp()
        self.token_generated = self.get_time()
        encode = jwt.encode({'iss': self.api_key, 'exp': self.token_expiration}, self.api_secret, algorithm='HS256',
                            headers={'typ': 'JWT'})
        return encode.decode('utf-8')
