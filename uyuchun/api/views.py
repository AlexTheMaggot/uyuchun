from django.http.response import JsonResponse
from admin.models import Header


def index(request):
    if request.method == 'POST':
        if request.POST['method'] == 'get_header':
            header = Header.objects.first()
            data = {
                'result': 'success',
                'content': {
                    'phone': header.phone,
                    'instagram': header.instagram,
                    'address': header.address,
                    'worktime': header.worktime,
                    'logo': header.logo.url,
                }
            }
        else:
            data = {
                'result': 'error',
            }
        return JsonResponse(data)
