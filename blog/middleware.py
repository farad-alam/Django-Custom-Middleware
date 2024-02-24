#funtion base middleware

def my_fun_middleware(get_response):
    # One time initilization goes here
    print('One time initilization data')
    def my_funtion(request):
        # before view code goes here
        print(' before view code')
        response = get_response(request)
        # after view code goes here
        print("after view code")
        return response
    return my_funtion

#class based middleware

class MyClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One time initilization code goes here")
    def __call__(self, request):
        # before view code goes here
        print("before view class bsased ")
        response =self.get_response(request)
        # after view code goes here
        print("after view class bsased ")
        return response
    
