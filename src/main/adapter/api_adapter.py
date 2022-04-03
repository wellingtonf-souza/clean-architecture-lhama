from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter pattern to Flask"""
    try:
        query = request.args.to_dict()
        if "pet_id" in query.keys():
            query["pet_id"] = int(query["pet_id"])
        if "user_id" in query.keys():
            query["user_id"] = int(query["user_id"])
    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    http_request = HttpRequest(header=request.headers, body=request.json, query=query)
    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    return response
