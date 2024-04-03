import json
import logging
from datetime import datetime

from fastapi import Response, Request
from pytz import timezone
from starlette.background import BackgroundTask
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import StreamingResponse
from starlette.types import Message

logger = logging.getLogger("main")
logging.basicConfig(level=logging.DEBUG, encoding='utf-8')
steam_handler = logging.FileHandler(filename='info.log', mode='w', encoding='utf-8')
logger.addHandler(steam_handler)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        req_client = request.client
        req_method = request.method
        req_url = request.url
        req_headers = request.headers
        req_body = await request.body()
        await set_body(request, req_body)
        response = await call_next(request)
        res_status_code = response.status_code
        res_media_type = response.media_type
        res_headers = response.headers
        if isinstance(response, StreamingResponse):
            res_body = b''
            async for chunk in response.body_iterator:
                res_body += chunk
        else:
            res_body = response.body
        task = BackgroundTask(func=log_info,
                              req_client=req_client,
                              req_method=req_method,
                              req_url=req_url,
                              req_headers=req_headers,
                              req_body=req_body,
                              res_status_code=res_status_code,
                              res_media_type=res_media_type,
                              res_headers=res_headers,
                              res_body=res_body)
        end_time = datetime.now()
        return Response(status_code=200,
                        media_type=res_media_type,
                        headers=dict(res_headers),
                        content=res_body,
                        background=task)


async def set_body(request: Request, body: bytes):
    async def receive() -> Message:
        return {'type': 'http.request', 'body': body}

    request._receive = receive


def log_info(req_client, req_method, req_url, req_headers, req_body,
             res_status_code, res_media_type, res_headers, res_body):
    try:
        decoded_res_body = res_body.decode('utf-8')
        if decoded_res_body.strip():
            res_body_to_print = json.loads(decoded_res_body)
        else:
            res_body_to_print = decoded_res_body
    except json.JSONDecodeError:
        res_body_to_print = res_body.decode('utf-8')

    logging.info("-" * 100)
    now = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f">>> REQUEST_TIME: {now}")
    logging.info(f">>> REQUEST_ADDRESS: {req_client}")
    logging.info(f">>> REQUEST_METHOD: {req_method}")
    logging.info(f">>> REQUEST_URL: {req_url}")
    logging.info(f">>> REQUEST_HEADER: {req_headers}")
    logging.info(f">>> REQUEST_BODY: {req_body.decode('utf-8')}")
    logging.info(f">>> RESPONSE_STATUS_CODE: {res_status_code}")
    logging.info(f">>> RESPONSE_MEDIA_TYPE: {res_media_type}")
    logging.info(f">>> RESPONSE_HEADER: {res_headers}")
    logging.info(f">>> RESPONSE_BODY : {res_body_to_print}")
    logging.info("-" * 100)
