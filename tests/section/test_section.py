from src.section import section

class TestSectionSerialize:
    def test_named_section(self):
        assert section({ "name": "cold", "key": "value" }) == (
            "[cold]\nkey = \"value\"\n")

    def test_anonymous_section(self):
        assert section({ "key": "value" }) == (
            "key = \"value\"\n")
