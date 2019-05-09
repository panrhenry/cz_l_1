import time
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    """统计首页每次访问程序所消耗的时间，也就是 Django 接受请求到最终返回的时间 """

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reversed('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response

    def process_expection(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self,request, response):
        costed = time.time()-self.start_time
        print('request to response cose: {:.2f}s'.format(costed))
        return response
