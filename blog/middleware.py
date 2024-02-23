
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
