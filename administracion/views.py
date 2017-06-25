from django.shortcuts import render

# Create your views here.
def index(request):
	return render_to_response('base.html',context_instance =RequestContext(request))