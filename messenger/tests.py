from django.test import TestCase
from messenger.services import valid_message, valid_mail


class ValidationTest(TestCase):
    """ validation tests """

    def test_mail_validation(self):
        mail1 = "test@test.ke"
        mail2 = "@test.ke"
        mail3 = "test@test"
        mail4 = "_@_.ke"
        mail5 = "qwe@qwe@qwe.qwe"
        mail6 = "qwe.qwe@qwe.qwe"
        mail7 = "test.com@test"
        mail8 = "valid@mail.com "
        mail9 = " valid@mail.com"

        self.assertTrue(valid_mail(mail1))
        self.assertFalse(valid_mail(mail2))
        self.assertFalse(valid_mail(mail3))
        self.assertTrue(valid_mail(mail4))
        self.assertFalse(valid_mail(mail5))
        self.assertTrue(valid_mail(mail6))
        self.assertFalse(valid_mail(mail7))
        self.assertFalse(valid_mail(mail8))
        self.assertFalse(valid_mail(mail9))

    def test_msg_validation(self):
        valid_msg = "Hello!"
        invalid_msg1 = "   "
        invalid_msg2 = "   "
        invalid_msg3 = "a" * 120
        self.assertTrue(valid_message(valid_msg))
        self.assertFalse(valid_message(invalid_msg1))
        self.assertFalse(valid_message(invalid_msg2))
        self.assertFalse(valid_message(invalid_msg3))
