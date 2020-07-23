import time
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
import pytz
class DurationTimeMiddleware(MiddlewareMixin):
    def process_request(self,request):
        request.request_time = time.time()
    def process_response(self, request,response):
        pass