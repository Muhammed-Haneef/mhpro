from django.urls import path
from mhadmin import views

urlpatterns=[
    path('index_page/',views.index_page,name="index_page"),
    path('addserv/',views.addserv,name="addserv"),
    path('adddesign/',views.adddesign,name="adddesign"),
    path('serviceadd/',views.serviceadd,name="serviceadd"),
    path('designadd/',views.designadd,name="designadd"),
    path('addproject/',views.addproject,name="addproject"),
    path('projectadd/',views.projectadd,name="projectadd"),
    path('displayservc/',views.displayservc,name="displayservc"),
    path('displaydesign/',views.displaydesign,name="displaydesign"),
    path('displayproject/',views.displayproject,name="displayproject"),
    path('editservc/<int:servcid>',views.editservc,name="editservc"),
    path('editdesign/<int:desid>',views.editdesign,name="editdesign"),
    path('editproject/<int:proid>',views.editproject,name="editproject"),
    path('deleteservc/<int:servcid>',views.deleteservc,name="deleteservc"),
    path('deldesign/<int:desid>',views.deldesign,name="deldesign"),
    path('deleteproject/<int:proid>',views.deleteproject,name="deleteproject"),
    path('updateservc/<int:servcid>',views.updateservc,name="updateservc"),
    path('updatedesign/<int:desid>',views.updatedesign,name="updatedesign"),
    path('updateproject/<int:proid>',views.updateproject,name="updateproject"),
    path('adlogin/',views.adlogin,name="adlogin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adlogout/',views.adlogout,name="adlogout"),
    path('contactdisplay/',views.contactdisplay,name="contactdisplay"),
    path('deletecontact/<int:cid>',views.deletecontact,name="deletecontact"),
    path('search/',views.search,name="search"),
    path('jobb_pg/',views.jobb_pg,name="jobb_pg"),
    path('addjob/',views.addjob,name="addjob"),
    path('disp_job/',views.disp_job,name="disp_job"),
    path('display_applicant/',views.display_applicant,name="display_applicant"),
    path('delete_appli/<int:apid>',views.delete_appli,name="delete_appli"),
    path('delete_job/<int:jobid>',views.delete_job,name="delete_job")

]