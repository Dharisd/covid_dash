from django.http import HttpResponse
from .models import QuarantineAddress,SampleDetail,ActiveCase
from django.template import loader


def index(request):
    all_addresses = QuarantineAddress.objects.all()
    active_cases = ActiveCase.objects.get()
    samples = SampleDetail.objects.get()
    template = loader.get_template('dash/index.html')

    context = {
        "q_addresses": all_addresses,
        "active_cases":active_cases,
        "samples":samples
    } 

    return HttpResponse(template.render(context, request))