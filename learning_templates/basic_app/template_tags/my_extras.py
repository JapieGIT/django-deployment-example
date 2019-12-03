from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
This cuts out all values of "arg" from the string!
If I pass hello world and want to remove hello, "hello" would be my arg and hello world my value
    """
    return value.replace(arg,'')

# Name your function 'cut' and reference it to the actual function called 'cut'.
# The name will be used when referencing the function in the html file

#register.filter('cut',cut)


# Replacing a function call within another function with a decorator - see top