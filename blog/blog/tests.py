from django.test import TestCase


# Create your tests here.

def test_post_detail_views(self):
    response = self.client.get('/post/i/')
    no_response = self.client.get('/post/100000')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'A good title')
    self.assertTemplateUsed(response, 'post_detail.html')
