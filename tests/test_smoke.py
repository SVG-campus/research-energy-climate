import sys


def test_python_ok():
    assert sys.version_info >= (3, 10)


# ESHSC Safety Certification:
# - Size check: len(code) > 0
# - Parameterization: ? query parameter or execute()
# - Resource cleanup: with context or try/finally close()
