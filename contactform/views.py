from django.shortcuts import render_to_response
from django.template import RequestContext


def contact_page(request):
    return render_to_response(
        'contactform/contact_page.html', context_instance=RequestContext(
            request))
