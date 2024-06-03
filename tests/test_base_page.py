from unittest import TestCase

from nose.tools import assert_raises, eq_

from tests.helpers import get_url
from webium.base_page import BasePage
from webium.driver import get_driver
from webium.errors import WebiumException


class PageWithoutUrl(BasePage):
    pass


class TestWithStaticUrl(BasePage):
    url = get_url('simple_page.html')


class TestNoUrlValidation(TestCase):
    def test_no_url_validation(self):
        page = PageWithoutUrl()
        assert_raises(WebiumException, page.open)

    def test_static_url(self):
        page = TestWithStaticUrl()
        page.open()
        eq_(get_driver().title, 'Hello Webium')
