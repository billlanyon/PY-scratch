import unittest
from unittest.mock import MagicMock
import json
from py_scratch.practise_python.WordDictionary import *
from test.TestBase import *

onlineoxford_pear = get_file_contents('Oxford_Pear.json')
pear_json = json.loads(onlineoxford_pear)


class HangmanTests(unittest.TestCase):

    def test_OnlineOxford_can_parse_its_own_json(self):
        oxford = OxfordOnlineWordDictionary()
        result =  oxford._extract_results(pear_json)
        self.assertEqual( ['1 : Old English pere, peru, of West Germanic origin; related to Dutch peer, '
                           'from Latin pirum',
                           '2 : a sweet yellowish- or brownish-green edible fruit that is typically '
                               'narrow at the stalk and wider towards the base, with sweet, slightly gritty flesh.',
                           '3 : the Eurasian tree which bears the pear.'], result )

    def test_LocalDictionary_making_internal_dict(self):
        internal_dict = LocalWordDictionary._make_internal_dict('LocalDictionary.csv')
        self.assertTrue('doe' in internal_dict.keys())

    def test_LocalDictionary_lookup_known_word(self):
        localDict = LocalWordDictionary('LocalDictionary.csv')
        self.assertEqual( ['1 : A deer a female deer'], localDict.lookup('doe'))

    def test_LocalDictionary_lookup_UNKNOWN_word(self):
        localDict = LocalWordDictionary('LocalDictionary.csv')
        self.assertEqual( ['UNKNOWN not found in LocalDictionary'], localDict.lookup('UNKNOWN'))

    def test_OnlineOxford_mocked_good_lookup(self):
        mock_requests = MagicMock()
        mock_result = MagicMock()
        mock_result.status_code = 200
        mock_result.text = onlineoxford_pear
        mock_requests.get.side_effect = [mock_result]
        oxford = OxfordOnlineWordDictionary(mock_requests)
        self.assertEqual(['1 : Old English pere, peru, of West Germanic origin; related to Dutch peer, '
                          'from Latin pirum',
                          '2 : a sweet yellowish- or brownish-green edible fruit that is typically '
                          'narrow at the stalk and wider towards the base, with sweet, slightly gritty flesh.',
                          '3 : the Eurasian tree which bears the pear.'], oxford.lookup('pear'))

    def test_OnlineOxford_mocked_word_not_found_lookup(self):
        mock_requests = MagicMock()
        mock_result = MagicMock()
        mock_result.status_code = 404
        mock_result.text = onlineoxford_pear
        mock_requests.get.side_effect = [mock_result]
        oxford = OxfordOnlineWordDictionary(mock_requests)
        self.assertEqual(['Oxford Online Dictionary could not find pear'], oxford.lookup('pear'))

    def test_OnlineOxford_did_not_respond_lookup(self):
        mock_requests = MagicMock()
        mock_result = MagicMock()
        mock_result.status_code = 999
        mock_result.text = onlineoxford_pear
        mock_requests.get.side_effect = [mock_result]
        oxford = OxfordOnlineWordDictionary(mock_requests)
        self.assertEqual(['Oxford Online Dictionary did not respond'], oxford.lookup('pear'))


if __name__ == '__main__':
    unittest.main()
