from django.urls import path

from mhuser import views

urlpatterns=[
    path('homepage/', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('projectpg/', views.projectpg, name="projectpg"),
    path('search_view/', views.search_view, name="search_view"),
    path('singlepropg/<proname>', views.singlepropg, name="singlepropg"),
    path('servicepg/', views.servicepg, name="servicepg"),
    path('news_pg/', views.news_pg, name="news_pg"),
    path('pricing_pg/', views.pricing_pg, name="pricing_pg"),
    path('estimate_pg/', views.estimate_pg, name="estimate_pg"),
    path('career_pg/', views.career_pg, name="career_pg"),
    path('applicant_pg/', views.applicant_pg, name="applicant_pg"),
    path('jobopeening/', views.jobopeening, name="jobopeening"),
    path('addnwsletr/', views.addnwsletr, name="addnwsletr"),
    path('singleservicepg/<servname>', views.singleservicepg, name="singleservicepg"),

]