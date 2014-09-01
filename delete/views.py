from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from delete.models import Car


@csrf_exempt
def delete(request, pk):
    if request.method == 'DELETE':
        Car.objects.get(pk=pk).delete()
        return HttpResponse("car with pk %s deleted" % pk, content_type='application/json')
    return HttpResponse("Not a delete request")
