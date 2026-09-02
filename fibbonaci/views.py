
from django.http import JsonResponse

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_view(request):
    count = int(request.GET.get('count', 10)) 
    gen = fibonacci_generator()
    numbers = [next(gen) for _ in range(count)]
    return JsonResponse({'fibonacci': numbers})
