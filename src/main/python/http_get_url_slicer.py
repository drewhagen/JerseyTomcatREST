'''
@date : 1.9.2018
@author : Drew Hagen
@script-reuse : OBJECTIVE
@description : SIMPLY slices a URL at the instance of the character '&',
    which properly splits the passed parameters within a query string in
    an HTTP GET request. (Often times started by a form submission)

EXAMPLE:
    INPUT: http://example.com/page?parameter=value&also=another
    This script looks at the String Query after the '?' in the url...
    Splits the String Query in new line at '&', and returns:
    OUTPUT:
        parameter=value
        also=another
'''

def get_params(url):
    str_query = url.split('?')[1]
    params = str_query.split('&')
    params_str = "\n".join(params)
    return params_str

def print_params(url):
    print get_params(url)

