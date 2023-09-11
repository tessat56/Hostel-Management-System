from django.urls import path
from .import views
#from .views import frontpage,home,about,ulogin,register,wardenlogin,studentpage,wardenpage,notification


from.views import home,success


urlpatterns = [

     
    path('',views.frontpage),
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    path('ulogin',views.ulogin),
    path('register',views.register),
    path('wardenlogin',views.wardenlogin),
    path('studentpage',views.studentpage),
    path('wardenpage',views.wardenpage),
    path('notifications',views.notification),
    path('wardenreg',views.wardenreg),
    path('wardenlogin',views.wardenlogin),
    path('sgatepass',views.sgatepass),
    path('sgprequest',views.sgprequest),
    path('sgpdisplay',views.sgpdisplay),
    path('sgpin',views.sgpin),
    path('viewgatepass',views.viewsgatepass),
    path('newgatereq',views.newgatereq),
    path('view<str:wk>',views.view,name="view"),
    path('accepted',views.accepted),
    path('rejected',views.rejected),
    path('gatepassin<str:gi>',views.gatepassin,name="gatepassin"),
    path('attendance',views.attendance),
    path('rooms',views.rooms),
    # path('save_checkbox_values/', views.save_checkbox_values),
    path('feedback_form', views.feedback_form),
   # path('viewmesscut', views.viewmesscut),

    
#tesse-g
    path('room_list', views.room_list, name='room_list'),
    path('room_detail<int:room_id>', views.room_detail, name='room_detail'),
    path('make_payment<int:room_id>', views.make_payment, name='make_payment'),
    path('menu/', views.menu,name='menu'),
    path('suggestion_list/', views.suggestion_list),

#tessa-t



     path('payment1',views.payment1),
     path('success1',views.success1),


#tessa-t

    path('slogout', views.slogout),


#rose

path('smess_cut_main/',views.smess_cut_main),
    path('smess_cut_main/smess_cutr/',views.smess_cutr),
    path('smess_cut_main/smess_cutd',views.smess_cutd),
    path('smess_cut_main/smess_cutr/smess_action',views.smess_action),

    path('vmess_cut/',views.vmess_cut),
    path('mess_cutview',views.mview),
    path('vmess_cut/vnewmessreq/',views.vnewmessreq),
    path('mview/<str:id>/',views.mview,name="mview"),
    path('vmess_cut/vnewmessreq/maccepted',views.maccepted),
    path('vmess_cut/vnewmessreq/mrejected',views.mrejected),

    path('grievance/', views.grievance, name='grievance'),
    path('grievance_list/', views.grievance_list, name='grievance_list'),

]

