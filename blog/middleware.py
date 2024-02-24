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
    
