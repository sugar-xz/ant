import pytest
from sparking import Sparking


class TestSparking(object):
    @pytest.mark.parametrize("bits_num, key, expected",[
        (8,5,2),
        (16,5,2),
        (32,5,2),
        (64,5,2)
    ])
    def test_get_num_of_one(self, bits_num, key, expected):
        assert Sparking.get_num_of_one(bits_num, key) == expected

    @pytest.mark.parametrize("bits_num, key, expected",[
        (8,5,6),
        (16,5,14),
        (32,5,30),
        (64,5,62)
    ])
    def test_get_num_of_zero(self, bits_num, key, expected):
        assert Sparking.get_num_of_zero(bits_num, key) == expected
