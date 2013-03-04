from __future__ import absolute_import

from django.conf.urls import patterns, url, include

from .views import (AgencyList, AgencyDetail, AgencyPositionDetail,
	AgencyDepartmentDetail, DepartmentLocationDetail, DepartmentEmployeeDetail,
	PersonList, PersonDetail)


urlpatterns = patterns('api.views',
    url(r'^$', 'api_root'),
    
    url(r'^v0/$', 'version_0', name='api-version-0'),
    
    url(r'^v0/agencies/$', AgencyList.as_view(), name='agency-list'),
    url(r'^v0/agencies/(?P<pk>[0-9]+)/$', AgencyDetail.as_view(), name='agency-detail'),

    url(r'^v0/agency_positions/(?P<pk>[0-9]+)/$', AgencyPositionDetail.as_view(), name='agencyposition-detail'),
    url(r'^v0/agency_departments/(?P<pk>[0-9]+)/$', AgencyDepartmentDetail.as_view(), name='agencydepartment-detail'),
    url(r'^v0/department_locations/(?P<pk>[0-9]+)/$', DepartmentLocationDetail.as_view(), name='departmentlocation-detail'),
    url(r'^v0/department_employees/(?P<pk>[0-9]+)/$', DepartmentEmployeeDetail.as_view(), name='departmentemployee-detail'),

    url(r'^v0/people/$', PersonList.as_view(), name='person-list'),
    url(r'^v0/people/(?P<pk>[0-9]+)/$', PersonDetail.as_view(), name='person-detail'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)
