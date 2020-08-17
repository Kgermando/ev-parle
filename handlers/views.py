from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.defaults import page_not_found
# Create your views here.
#Bad request
def handler400(request):
	return render(request,  template_name='base/handlers/400.html')
	response.status_code = 400
	return response

#Permission denied
def handler403(request):
	return render(request,  template_name='base/handlers/403.html')
	response.status_code = 403
	return response

#Page not found
def handler404(request):
	return render(request,  template_name='base/handlers/404.html')
	response.status_code = 404
	return response

#Server error
def handler500(request):
	return render(request,  template_name='base/handlers/500.html')
	response.status_code = 500
	return response