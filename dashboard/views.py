from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
<<<<<<< HEAD
    organisation=Organisation.objects.filter(organisation_name=request.user.profile.organisation.organisation_name)

    context={
            'organisation': organisation[0],
            'media_url': settings.MEDIA_URL,
        }
    return render(request,"index.html", context)
  
=======
    return render(request,"index.html")
>>>>>>> parent of 740ccec... ✔ Invoice bug fix
