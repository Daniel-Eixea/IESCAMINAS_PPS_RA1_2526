from Apartado1.app_cifrado import sha512, sha256, md5, sha1, caesar


def test_sha256():
    assert sha256(b"Hello world") == "64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c"

def test_sha512():
    assert sha512(b"Hello world") == "b7f783baed8297f0db917462184ff4f08e69c2d5e5f79a942600f9725f58ce1f29c18139bf80b06c0fff2bdd34738452ecf40c488c22a7e3d80cdf6f9c1c0d47"

def test_md5():
    assert md5(b"Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_sha1():
    assert sha1(b"Hello world") == "7b502c3a1f48c8609ae212cdfb639dee39673f5e"

def test_caesar():
    assert caesar("Hello world", 3) == "Khoor zruog"
    assert caesar("Khoor zruog", -3) == "Hello world"