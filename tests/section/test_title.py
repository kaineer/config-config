from src.section import title

class TestSectionTitle:
    def test_unnamed_title(self):
        assert title(None) == ''

    def test_simple_title(self):
        assert title("simple") == "[simple]\n"

    def test_dotted_title(self):
        assert title("outer.inner") == "[\"outer.inner\"]\n"
