from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'survey'

urlpatterns = [
	path('', views.surveys, name='surveys'),
	path('<int:survey_id>', views.survey, name='survey-home'),
	path('<int:survey_id>/submitVote/', views.submitVote, name='submitVote'),
	path('results', views.results, name='survey-results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
