from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import Organisation

# Create your views here.
@login_required
def index(request):
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"index.html", context)
  