from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^image_code/([\w-]+)/$',views.ImageView.as_view()),
    # url(r'^image_code/(?P<image_id>[\w-]+)/$',views.ImageView.as_view()),
    url(r'msg_code/',views.MsgView.as_view()),
# GET  /msg_code/?image_id=uuid&image_text=mytext&phone=12345678

]
