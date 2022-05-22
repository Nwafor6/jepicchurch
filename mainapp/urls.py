from django.urls import path
from .views import *
from . import views

urlpatterns=[

	path('', HomePageView.as_view(), name='home'),

	path('contact-us/', ContactPageView.as_view(), name='contact-page'),

	path('prayer-request/', SubmitPageView.as_view(), name='prayer-request'),

	path('about/children-ministry/', ChildrenMinistryPageView.as_view(), name='children-ministry'),

	path('about/our-belive/', OurBelivePageView.as_view(), name='our-belive'),

	path('about/our-history/', OurHistoryPageView.as_view(), name='our-history'),

	path('media/gallery/', GalleryListView.as_view(), name='gallery'),

	path('media/gallery-image/<int:pk>/', OurGalleryPageView.as_view(), name='gallery-image'),

	path('upcoming-event/<slug:slug>/', EventDetailPageView.as_view(), name='event-detail'),

	# path('media/galery/', EventDetailPageView.as_view(), name='gallery'),

	path('media/gallery-form/', GalleryCreateView.as_view(), name='gallery-form'),
	


]