from __future__ import unicode_literals

from django.urls import reverse

from mayan.apps.rest_api.tests import BaseAPITestCase


class EventAPITestCase(BaseAPITestCase):
    def test_evet_type_list_view(self):
        response = self.client.get(reverse(viewname='rest_api:event-type-list'))
        self.assertEqual(response.status_code, 200)
