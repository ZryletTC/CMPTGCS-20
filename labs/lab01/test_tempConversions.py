from tempConversions import *

def test_temp_conversions_fToC_32_0():
    assert fToC(32.0) == 0.0

def test_temp_conversions_fToC_212_100():
    assert fToC(212.0) == 100.0

def test_temp_conversions_cToF_0_32():
    assert cToF(0.0) == 32.0

def test_temp_conversions_cToF_100_212():
    assert cToF(100.0) == 212.0
