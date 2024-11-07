from src.serialize import serialize

class TestSerializeValue:
    def test_serialize_number(self):
        assert serialize(42) == "42"

    def test_serialize_boolean(self):
        assert serialize(True) == "true"
        assert serialize(False) == "false"

    def test_serialize_string(self):
        assert serialize("simple") == "\"simple\""
        assert serialize("\xce\xb2") == "\"β\""

    def test_serialize_list(self):
        assert serialize([]) == "[]"
        assert serialize([[], 1]) == "[[], 1]"
        assert serialize([True, 41, "string"]) == "[true, 41, \"string\"]"
