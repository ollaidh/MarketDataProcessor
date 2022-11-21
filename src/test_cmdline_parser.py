import unittest
import cmdline_parser


class TestArgsParse(unittest.TestCase):
    def test_parse(self):
        self.assertRaises(SystemExit, cmdline_parser.parse, [])

        conf = cmdline_parser.parse(['--config=config.json'])
        self.assertEqual(conf.config, 'config.json')

        conf = cmdline_parser.parse(['--config', 'another_config.json'])
        self.assertEqual(conf.config, 'another_config.json')

        conf = cmdline_parser.parse(['-cshort_config.json'])
        self.assertEqual(conf.config, 'short_config.json')


if __name__ == '__main__':
    unittest.main()
