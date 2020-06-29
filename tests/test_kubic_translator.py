from unittest import TestCase

from kubic.command import KubicCommand
from kubic.translator import KubicTranslator


class TestKubicTranslator(TestCase):
    TEST_DATA = 'kubectl get pod'

    def setUp(self):
        translator = KubicTranslator()
        self.translator_returned = translator.run(self.__class__.TEST_DATA)

    def test_run_and_return_kubic_command(self):
        self.assertIsInstance(self.translator_returned, KubicCommand)