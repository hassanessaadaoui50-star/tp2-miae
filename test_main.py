import subprocess
import sys
import unittest


class TestMain(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(
            [sys.executable, "main.py"], capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "hello MIAE")


if __name__ == "__main__":
    unittest.main()
