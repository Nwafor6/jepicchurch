from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Upcoming_Event
from django.views.generic.edit import CreateView
from django.forms import modelformset_factory
from .forms import *
from.models import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomePageView (TemplateView):
	template_name='mainapp/index.html'

class ContactPageView (TemplateView):
	template_name='mainapp/contact-us.html'

class SubmitPageView (TemplateView):
	template_name='mainapp/submit-prayer-request.html'

class ChildrenMinistryPageView (TemplateView):
	template_name='mainapp/children-ministry.html'

class OurBelivePageView (TemplateView):
	template_name='mainapp/our-belive.html'

class OurHistoryPageView (TemplateView):
	template_name='mainapp/our-history.html'


class GalleryCreateView (LoginRequiredMixin,CreateView):
	model=Gallery
	form_class=GalleryForm
	template_name='mainapp/gallery-form.html'
	success_url='/media/gallery/'

	# def get_form(self, *args, **kwargs):
	# 	user=self.request.user
	# 	form=super().get_form(*args, **kwargs)

	def get (self, request, *args, **kwargs):

		form=GalleryForm()
		context={'form':form}
		return render (request, self.template_name, context)


	def post(self, request, *args, **kwargs):
		form=GalleryForm(request.POST, request.FILES)
		if form.is_valid():
			data=form.cleaned_data
			user=request.user
			gallery=form.save(commit=False)
			gallery.user=user
			images=request.FILES.getlist('image')
			if images:
				gallery.save()
				form.save_m2m()

				for image in images:
					gallery_images =GalleryImage.objects.create(
						gallery=gallery,
						image=image
						)
					gallery_images.save()
				return redirect (self.success_url)

			else:

				form.add_error("image", "unable to list item add an image to the gallery.")

		context={'form':form}
		return render (request, self.template_name, context)





class GalleryListView(ListView):
	model=Gallery
	template_name='mainapp/gallery.html'
	context_object_name='event'

	
	# def get_context_data(self, *args, **kwargs):

	# 	context=super().get_context_data(**kwargs)
	# 	q=Gallery.objects.get(pk=self.kwargs['pk'])
	# 	context['event']=GalleryImage.objects.all()
	# 	context['images']=q.galleryimage_set.all()
	# 	return context

	# def get_context_data(self, *args, **kwargs):
	# 	context=super().get_context_data(**kwargs)
	# 	context['event']=Gallery.objects.all()
	# 	context['images']=GalleryImage.objects.all()
	# 	return context



class OurGalleryPageView (DetailView):
	model=GalleryImage
	template_name='mainapp/gallery-detail.html'
	# context_object_name='images'

	

	def get_context_data(self, *args, **kwargs):

		context=super().get_context_data(**kwargs)
		q=Gallery.objects.get(pk=self.kwargs['pk'])
		context['Gallery']= Gallery.objects.get(pk=self.kwargs['pk'])
		context['images']=q.galleryimage_set.all()
		return context



class EventDetailPageView (DetailView):
	model=Upcoming_Event
	template_name='mainapp/event.html'
	context_object_name='event'

	# def get_context_data(self, *args, **kwargs):
	# 	context=super().get_context_data(**kwargs)
	# 	context['event']=Upcoming_Event.objects.get(slug=self.kwargs['slug'])[:1]


# def get(request, pk):
# 	gallery=Gallery.objects.get(pk=pk)
# 	gallery_image=gallery_image_set.all()
# 	context={'gallery':gallery, 'gallery_image':gallery_image}
# 	return render(request, 'main.gallery-detail.html', context)





		    
		

