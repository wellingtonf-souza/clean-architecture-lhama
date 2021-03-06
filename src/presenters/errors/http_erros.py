class HttpErrors:
    """Class to define erros in http"""

    @staticmethod
    def error_422():
        """422"""
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        """400"""
        return {"status_code": 400, "body": {"error": "Bad request"}}

    @staticmethod
    def error_409():
        """409"""
        return {"status_code": 409, "body": {"error": "Conflict"}}
