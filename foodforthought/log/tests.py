from django.test import TestCase, Client 

client = Client()

class UrlTestCase(TestCase):
    def test_choose_level(self):
        level = self.client.get('/log/level')
        self.assertEqual(level.status_code, 200)

    def test_show_question(self):
        question = self.client.get('/log/question')
        self.assertEqual(question.status_code, 200)

    def test_notify_success(self):
        success = self.client.get('/log/success')
        self.assertEqual(success.status_code, 200)

    def test_notify_failure(self):
        failure = self.client.get('/log/failure')
        self.assertEqual(failure.status_code, 200)

    def test_choose_reward(self):
        reward = self.client.get('/log/reward')
        self.assertEqual(reward.status_code, 200)

    def test_redirect_to_journal(self):
        journal = self.client.get('/log/to_journal')
        self.assertEqual(journal.status_code, 200)

    
