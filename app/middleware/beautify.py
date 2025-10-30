from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.templating import Jinja2Templates
from typing import Any, Dict, Union
import json
from datetime import datetime

# Initialize templates with absolute path
templates = Jinja2Templates(directory="/company_portal_service/app/templates")

class BeautifyMiddleware:
    async def __call__(self, request: Request, call_next):
        # Get the original response
        response = await call_next(request)
        
        # Skip beautification if any of these conditions are met:
        should_skip = (
            # Skip Swagger UI and ReDoc routes
            request.url.path.startswith("/docs") or
            request.url.path.startswith("/redoc") or
            request.url.path.startswith("/openapi.json") or
            # Skip if client specifically asks for JSON
            request.headers.get("accept") == "application/json" or
            # Skip if it's already an HTML response
            isinstance(response, HTMLResponse)
        )
        
        if should_skip:
            return response

        try:
            # Convert response to JSON data
            if hasattr(response, 'body'):
                # For JSONResponse
                raw_response = response.body.decode()
            else:
                # For StreamingResponse and other response types
                response_body = [chunk async for chunk in response.body_iterator]
                raw_response = b''.join(response_body).decode()

            # Parse the JSON data
            try:
                data = json.loads(raw_response)
            except json.JSONDecodeError:
                # If it's not JSON data, return original response
                return response

            # Create HTML response
            return templates.TemplateResponse(
                "response.html",
                {
                    "request": request,
                    "data": data,
                    "title": f"Response - {request.url.path}",
                    "status_code": response.status_code,
                    "endpoint": request.url.path,
                    "now": datetime.now
                },
                status_code=response.status_code
            )
        except Exception as e:
            print(f"Error in middleware: {str(e)}")  # Debug log
            return response