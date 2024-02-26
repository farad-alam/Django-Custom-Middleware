from django.shortcuts import HttpResponse

#funtion base middleware

# def my_fun_middleware(get_response):
#     # One time initilization goes here
#     print('One time initilization data')
#     def my_funtion(request):
#         # before view code goes here
#         print(' before view code')
#         response = get_response(request)
#         # after view code goes here
#         print("after view code")
#         return response
#     return my_funtion

#class based middleware

# class MyClassMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time initilization code goes here")
#     def __call__(self, request):
#         # before view code goes here
#         print("before view class bsased ")
#         response =self.get_response(request)
#         # after view code goes here
#         print("after view class bsased ")
#         return response


# class MyClassMiddlewareTwo:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time initilization code goes here Two")
#     def __call__(self, request):
#         # before view code goes here
#         print("before view class bsased Two")
#         response = self.get_response(request)

#         # response = HttpResponse(" Retunning response from middleware two")
#         # (returnning response from this middlleware)

#         # after view code goes here
#         print("after view class bsased Two")
#         return response

# class MyClassMiddlewareThree:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time initilization code goes here Three")
#     def __call__(self, request):
#         # before view code goes here
#         print("before view class bsased Three")
#         response =self.get_response(request)
#         # after view code goes here
#         print("after view class bsased Three")
#         return response

class MyProcessViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, *args, **kwargs):
        print("this is process view - before view")
        # return HttpResponse('returned from process view')
        return None
    
    def process_exception(self, request, exception):
        msg = exception
        print(msg)
        print(exception.__class__.__name__)
        return HttpResponse(msg)
    
    def process_template_response(self, request, response):
        response.context_data['author'] = 'Shifa'
        return response
    



from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
import time

class RateLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        # Get the client's IP address
        ip_address = request.META.get('REMOTE_ADDR')

        # Define the rate limit parameters
        limit = 100  # Max requests per minute
        period = 60  # Time window in seconds

        # Generate a unique key for the client's IP address
        key = f'ratelimit:{ip_address}'

        # Get the current count of requests from the cache
        count = cache.get(key, 0)

        # If the count is above the limit, reject the request
        if count >= limit:
            return HttpResponseForbidden("Rate limit exceeded")

        # Increment the count and update the cache
        cache.set(key, count + 1, period)

        # Add a custom header to the response indicating the remaining requests
        remaining_requests = limit - (count + 1)
        response = self.get_response(request)
        response['X-RateLimit-Remaining'] = str(remaining_requests)

        return None
