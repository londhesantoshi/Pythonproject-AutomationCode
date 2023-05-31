import base64


class Decode:

    def decode_password(self,encodedstring):
        return base64.b64decode(encodedstring).decode("UTF-8")

