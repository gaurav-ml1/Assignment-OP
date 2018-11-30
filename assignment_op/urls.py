from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [

    # ---django admin--- #
    url(r'^admin/', admin.site.urls),

    # ---api to access product app--- #
    url('api/v1/', include("product.urls")),

    # --- Home page (Product table)--- #
    url(r"^$", TemplateView.as_view(template_name="home.html"), name="home")

]