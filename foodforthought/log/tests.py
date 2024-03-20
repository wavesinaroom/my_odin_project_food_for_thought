from django.test import TestCase, Client 

client = Client()

class Question(TestCase):
    def test_show_question_view(self):
        question = self.client.get('/log/question')
        self.assertEqual(question.status_code, 200)
        self.assertEqual(question['content-type'], 'text/html; charset=utf-8')
        self.assertTemplateUsed(question, "log/question.html")
