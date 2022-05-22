from .models import Upcoming_Event, GalleryImage


def EventTemplatePageView(request):
	return {'events':Upcoming_Event.objects.all().order_by('-title')[:1] }

def footergallery(request):
	return{'footer_gallery':GalleryImage.objects.all()[:8]}

