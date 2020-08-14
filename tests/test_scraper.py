import unittest
import utils
import os


class SeleniumTestCases(unittest.TestCase):
    def setUp(self):
        os.environ["binary_path"] = os.getcwd(
        )+"/venv/chrome/headless-chromium"
        os.environ["executable"] = os.getcwd()+"/venv/chrome/chromedriver"

    def test_
    def test_javascript_render(self):
        items = 0
        results = self.sel_obj.list_elements_on_page()
        for quote in next(results):
            quoteArr = quote.text.split('\n')
            self.assertEqual(type(quoteArr), list)
            self.assertEqual(type(quoteArr[0]), str)
            self.assertEqual(quoteArr[1], utils.json_read_from_file("scrape_queries.json")["test_data"]["search_query"])
            items += 1
        self.assertTrue(items > 1)

    def test_find_by_class(self):
        self.sel_obj.find_by_class = True
        self.sel_obj.find_by_id = False
        self.sel_obj.element_to_find = "m-brick"
        self.test_javascript_render()

    def test_find_by_neither(self):
        self.sel_obj.find_by_class = False
        self.sel_obj.find_by_id = False
        results = self.sel_obj.list_elements_on_page()
        with self.assertRaises(Exception):
            next(results)

    def tearDown(self):
        self.sel_obj.stop_driver()
