def log():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            print(request.headers)
            print(request.get_full_path())
            print(get_client_ip(request))
            # ToDo: into elasticsearch
            return func(request, *args, **kwargs)

        return wrapper

    return decorator


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
