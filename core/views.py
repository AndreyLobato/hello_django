

from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request,n1, n2):
    som = n1 + n2
    sub = n1 - n2
    mul = n1 * n2
    div = n1 / n2

    return HttpResponse('A soma é: {}\n'
                        'A subtração: {}\n'
                        'A multiplicação: {}\n'
                        'A Divisão:{}\n'.format(som, sub, mul, div))



"""
    return HttpResponse('<h1>A soma é: {}\n'
                        'A subtração: {}\n'
                        'A multiplicação: {}\n'
                        'A Divisão:{}\n</h1>'.format(som,sub,mul,div))

return HttpResponse('<h1>A soma é: {}</h1>'
                        '<h2>A subtração: {}</h2>'
                        '<h3>A multiplicação: {}</h3>'
                        '<h4>A Divisão:{}</h4>>'.format(som,sub,mul,div))
"""





