import contextlib
import io
import unittest

from slug import main, slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_accents(self):
        self.assertEqual(slugify("Café au lait"), "cafe-au-lait")

    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")


class MaxLengthTest(unittest.TestCase):
    def test_no_limit_unchanged(self):
        self.assertEqual(slugify("Hello, World!", None), "hello-world")

    def test_short_enough(self):
        self.assertEqual(slugify("Hello, World!", 11), "hello-world")
        self.assertEqual(slugify("Hello, World!", 50), "hello-world")

    def test_cuts_at_dash(self):
        # "the-quick-brown-fox"[:12] is "the-quick-br"; back off to the last dash.
        self.assertEqual(slugify("The quick brown fox", 12), "the-quick")

    def test_cut_ending_on_word_boundary(self):
        # The next character is a dash, so the whole word fits.
        self.assertEqual(slugify("The quick brown fox", 9), "the-quick")

    def test_no_trailing_dash(self):
        self.assertEqual(slugify("The quick brown fox", 10), "the-quick")

    def test_single_long_word_is_cut(self):
        self.assertEqual(slugify("Supercalifragilistic", 5), "super")
        self.assertEqual(slugify("Supercalifragilistic day", 5), "super")

    def test_zero(self):
        self.assertEqual(slugify("Hello", 0), "")


class MainTest(unittest.TestCase):
    def run_main(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = main(argv)
        return code, out.getvalue()

    def test_without_option(self):
        self.assertEqual(self.run_main(["Hello, World!"]), (0, "hello-world\n"))

    def test_max_length(self):
        self.assertEqual(
            self.run_main(["--max-length", "12", "The quick brown fox"]),
            (0, "the-quick\n"),
        )

    def test_negative_max_length_rejected(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            main(["--max-length", "-1", "Hello"])
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
