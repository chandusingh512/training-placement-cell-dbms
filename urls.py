from django.conf.urls import url
from . import views

app_name='tcp'
urlpatterns = [
	url(r'^$', views.indexx , name='indexx'),
	url(r'^test/$', views.test , name='test'),
	url(r'^statistics/$', views.statistics, name='statistics'),
	url(r'^student_signup/$', views.student_signup , name='student_signup'),
	url(r'^faculty_signup/$', views.faculty_signup , name='faculty_signup'),
	url(r'^faculty_signup/tcp/faculty_signup/$', views.faculty_signup , name='faculty_signup'),
	url(r'^admin_signup/$', views.admin_signup , name='admin_signup'),
	url(r'^admin_signup/tcp/admin_signup/$', views.admin_signup , name='admin_signup'),
	url(r'^login/$', views.login , name='login'),
	url(r'^student_signup/tcp/firstlook/$', views.firstlook , name='firstlook'),
	url(r'^faculty/tcp/firstlook$', views.firstlook , name='firstlook'),
	url(r'^admin/tcp/firstlook$', views.firstlook , name='firstlook'),
	url(r'^login/tcp/firstlook$', views.firstlook , name='firstlook'),
	url(r'^login/tcp/student/web/index$', views.index , name='index'),
	url(r'^student_signup/tcp/student/web/index/$', views.index , name='index'),
	url(r'^admin/tcp/admin/web/index$', views.indexzz , name='indexzz'),
	url(r'^faculty/tcp/faculty/web/index$', views.indexz , name='indexz'),
	#url(r'^student_signup/tcp/student/web/tcp/student/web/details/student_reg$', views.student_reg , name='student_reg'),
	url(r'^admin/tcp/admin/web/tcp/admin/web/details/admin_reg$', views.admin_reg , name='admin_reg'),
	url(r'^faculty/tcp/faculty/web/tcp/faculty/web/details/faculty_reg$', views.faculty_reg , name='faculty_reg'),
	url(r'^student_signup/tcp/student/web/tcp/student/web/reg/test_registration$', views.test_registration , name='test_registration'),
	url(r'^faculty/tcp/faculty/web/tcp/faculty/web/reg/update_materials$', views.update_materials , name='update_materials'),
	url(r'^admin/tcp/admin/web/tcp/admin/web/reg/web/company_details$', views.company_details , name='company_details'),
	url(r'^student_signup/tcp/student/web/tcp/student/web/reg/tcp/student_signup/tcp/student/web/index$', views.index, name='index'),
	url(r'^admin/tcp/admin/web/tcp/admin/web/reg/web/tcp/admin/web/indexzz' , views.indexzz, name='indexzz'),
	url(r'^faculty/tcp/faculty/web/tcp/faculty/web/reg/tcp/faculty/tcp/faculty/web/index', views.indexz, name='indexz'),
	url(r'^student_signup/tcp/student/web/tcp/student/web/details/tcp/student/web/index' , views.index, name='index'),
	url(r'^faculty/tcp/faculty/web/tcp/faculty/web/details/tcp/faculty/web/indexz' , views.indexz, name='indexz'),


	url(r'^login/tcp/student/web/details/index/$', views.index_details , name='index_details'),
	url(r'^student/web/details/index_details/$', views.index_details , name='index_details'),

	url(r'^login/tcp/student/web/reg/web/test_registration$', views.test_registration , name='test_registration'),
	url(r'^login/tcp/student/web/reg/web/tcp/student/web/reg/web/test_registration$', views.test_registration , name='test_registration'),
	url(r'^login/tcp/student/web/reg/web/test_registration$', views.test_registration , name='test_registration'),


	url(r'^login/tcp/faculty/web/details/faculty_reg/$', views.faculty_reg , name='faculty_reg'),
	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/$', views.faculty_reg , name='faculty_reg'),

	url(r'^login/tcp/admin/web/details/admin_reg/$', views.admin_reg , name='admin_reg'),
	url(r'^admin/web/details/admin_reg/$', views.admin_reg , name='admin_reg'),

	url(r'^login/tcp/admin/web/reg/web/company_details/$', views.company_details , name='company_details'),
	url(r'^login/tcp/admin/web/reg/web/company_details/tcp/admin/web/reg/web/company_details/$', views.company_details , name='company_details'),

	url(r'^login/tcp/faculty/web/reg/update_materials/$', views.update_materials , name='update_materials'),
	url(r'^login/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/$', views.update_materials , name='update_materials'),

	url(r'^admin_signup/firstlook/$' , views.firstlook, name='firstlook'),
	

	url(r'^faculty_signup/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^firstlook/$' , views.firstlook, name='firstlook'),


	url(r'^test/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^statistics/firstlook/$' , views.firstlook, name='firstlook'),


	url(r'^login/tcp/faculty/web/placement/$' , views.placement_reg , name='placement_reg'),
	url(r'^faculty/web/placement_reg/$' , views.placement_reg , name='placement_reg'),

	url(r'^faculty/firstlook/$' , views.firstlook, name='firstlook'),


	url(r'^login/tcp/student/web/reg/web/tcp/student/web/reg/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^login/tcp/student/web/reg/web/tcp/student/web/reg/web/firstlook/$', views.firstlook , name='firstlook'),

	url(r'^test/tcp/student/web/reg/web/test_registration/$' , views.test_registration , name='test_registration'),
	url(r'^test/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/test_registration/$' , views.test_registration, name='test_registration'),

	url(r'^test/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/firstlook/$' , views.firstlook , name='firstlook'),
	url(r'^login/tcp/admin/web/reg/web/company_details/tcp/admin/web/reg/firstlook/$', views.firstlook , name='firstlook'),
	
	url(r'^test/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/test_registration/firstlook/$', views.firstlook , name='firstlook'),
	
	url(r'^login/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^student/web/details/firstlook/$' , views.firstlook, name='firstlook'),

	url(r'^faculty_signup/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^admin_signup/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	
	url(r'^login/tcp/faculty/web/placement/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	url(r'^faculty_signup/tcp/faculty_signup/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^admin_signup/tcp/admin_signup/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^firstlook/$' , views.firstlook, name='firstlook'),
	
	
	url(r'^student_signup/tcp/student/web/reg/web/test_registration/$' , views.test_registration , name='test_registration'),
	url(r'^student_signup/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/test_registration/$' , views.index, name='index'),
	url(r'^student_signup/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/$', views.faculty_reg , name='faculty_reg'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/$', views.indexz , name='indexz'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/firstlook/$' , views.firstlook , name='firstlook'),
	
	
	url(r'^admin_signup/tcp/admin_signup/tcp/admin/web/details/admin_reg/$', views.admin_reg , name='admin_reg'),
	url(r'^admin/web/details/admin_reg/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^login/tcp/admin/web/reg/web/company_details/tcp/admin/web/reg/web/company_details/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/reg/update_materials/$', views.update_materials , name='update_materials'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/$' , views.indexz, name='indexz'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	url(r'^student_signup/tcp/student/web/details/index/$', views.index_details , name='index_details'),
	url(r'^student_signup/tcp/student/web/placement/$', views.test , name='test'),
	
	
	url(r'^student_signup/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/$' , views.test_registration, name='test_registration'),
	url(r'^student_signup/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/test_registration/$' , views.index, name='index'),
	url(r'^student_signup/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	
	url(r'^login/tcp/student/web/placement/$', views.test , name='test'),
	url(r'^login/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/$' , views.test_registration, name='test_registration'),
	
	url(r'^login/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/test_registration/$' , views.index, name='index'),
	url(r'^login/tcp/student/web/placement/tcp/student/web/reg/web/test_registration/tcp/student/web/reg/web/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	
	
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/placement/$' , views.placement_reg , name='placement_reg'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/placement/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^faculty/web/placement_reg/tcp/firstlook/$' , views.firstlook, name='firstlook'),


	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/$', views.update_materials , name='update_materials'),

	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/$' , views.indexz, name='indexz'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/faculty/web/placement/$' , views.placement_reg , name='placement_reg'),


	url(r'^faculty_signup/tcp/faculty_signup/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/faculty/web/placement/firstlook/$' , views.firstlook, name='firstlook'),

	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/$', views.update_materials , name='update_materials'),
	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/placement/$' , views.placement_reg , name='placement_reg'),



	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/$' , views.indexz, name='indexz'),

	url(r'^login/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/details/faculty_reg/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/firstlook/$' , views.firstlook, name='firstlook'),

	url(r'^login/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^login/tcp/faculty/web/reg/update_materials/tcp/faculty/web/reg/web/update_materials/tcp/faculty/web/details/faculty_reg/$', views.faculty_reg , name='faculty_reg'),

	url(r'^login/tcp/student/web/reg/web/study_materials/$', views.study_materials , name='study_materials'),
	url(r'^login/tcp/student/web/reg/web/study_materials/firstlook/$' , views.firstlook, name='firstlook'),



	url(r'^student_signup/tcp/student/web/reg/web/study_materials/$', views.study_materials , name='study_materials'),
	url(r'^student_signup/tcp/student/web/reg/web/study_materials/firstlook/$' , views.firstlook, name='firstlook'),
	
	
	
	url(r'^student_signup/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^student/web/details/index_details/tcp/student/web/reg/web/study_materials/$', views.study_materials , name='study_materials'),
	url(r'^student/web/details/index_details/tcp/student/web/placement/firstlook/$' , views.firstlook, name='firstlook'),
	url(r'^student/web/details/index_details/tcp/student/web/placement/$', views.test , name='test'),
	
	url(r'^login/tcp/student/web/placement/firstlook/$' , views.firstlook, name='firstlook'),
	
]