import unittest

from agent_orchestration import __version__


class PackageTests(unittest.TestCase):
    def test_version_is_available(self) -> None:
        self.assertEqual(__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
