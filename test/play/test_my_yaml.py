import unittest
import play.my_yaml as my_yaml
import datetime


class MyYamlTestCase(unittest.TestCase):

    def test_read_mapping(self):
        self.assertEqual('venkatray', my_yaml.read_mapping('firstName'))
        self.assertEqual('kamath', my_yaml.read_mapping('last Name'))

    def test_read_list(self):
        self.assertEqual(['UBS', 'Lehman', 'JP Morgan & Chase'], (my_yaml.read_list('companies')))

    def test_read_date(self):
        self.assertEqual(datetime.date, type(my_yaml.read_mapping('graduatedOn')))
        self.assertEqual(datetime.date(2002, 06, 01), my_yaml.read_mapping('graduatedOn'))

    def test_read_multi_line_string(self):
        expected = '''this is my first experience
with yaml and python. wow. pretty cool !!!'''
        self.assertEqual(expected, my_yaml.read_mapping('note'))


