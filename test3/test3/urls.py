"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from myapp.views import *
import myapp
from myapp import views
app_name = 'myapp'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^deo/$', deo),
    url(r'^deo/deo_submit/$', deo_submit),
    url(r'^deo/deo_submit/deo_profile', deo_profile),
    url(r'^hod/$', hod),
    url(r'^hod/selection/', selection),
    url(r'^hod/selection_inter/', selection_interview),
    url(r'^hod/selection_cv/(\d+)/', selection_cv),
    url(r'^hod/selection_profile/(\d+)/', selection_profile),
    url(r'^hod/post_list/$', hod_post_list),
    url(r'^hod/hod_vacancy/(\d+)/$', hod_vacancy),
    url(r'^hod/hod_vacancy/succs/$', hod_vacancy_succs),
    url(r'^hod/hod_vacancy/test/$', hod_vacancy_test),
    url(r'^hod/hod_vacancy/test/(\d+)/$', hod_inter_create),
    url(r'^hod/hod_vacancy/test/succs/$', hod_inter_create_succs),
    url(r'^hod/hod_vacancy/test/part2/inter_list/$', hod_inter_list_interviewer),
    url(r'^hod/hod_vacancy/test/part2/inter_list/(\d+)/$', hod_pre_interviwer_list, name="inter1"),
    url(r'^hod/hod_vacancy/test/part2/inter_list/(\d+)/(\d+)/$', hod_inter_interviewer_2, name="inter2"),
    url(r'^hod/hod_vacancy/test/part2/inter_list_cv/$', hod_inter_list_cv),
    url(r'^hod/hod_vacancy/test/part2/inter_list_cv/(\d+)/$', hod_pre_cv_list, name="cv1"),
    url(r'^hod/hod_vacancy/test/part2/inter_list_cv/(\d+)/(\d+)/$', hod_inter_cv, name="cv2"),
    url(r'^hod/hod_vacancy/test/vacancy/(?P<ID>[0-9]+)/$', hod_view_vacancy),
    url(r'^hod/hod_cv/$', hod_cv),
    url(r'^hod/hod_cv/(\d+)/$', hod_profile),
    url(r'^hod/hod_cv/cv_list/(\d+)/', hod_cv_list),
    url(r'^hod/hod_inter/$', hod_inter),
    url(r'^hod/hod_inter/chs_vacn/$', hod_inter_choose_vacancy),
    url(r'^hod/hod_vacancy/test/part2/$', hod_inter_cv),
    url(r'^hod/hod_inter/hod_pre_inter_overview/$', hod_pre_inter_vacancy_overview),
    url(r'^hod/hod_inter/hod_inter_overview/(\d+)$', hod_inter_overview),
    url(r'^hod/hod_inter/hod_inter_overview/view/(\d+)', hod_inter_view),
    url(r'^hod/hod_inter/hod_succs$', hod_succs),
    url(r'^hod/hod_msg/$', hod_msg),
    url(r'^sub/$', subv),

]
