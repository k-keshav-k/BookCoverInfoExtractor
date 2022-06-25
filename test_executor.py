from executor import MainExecutor
import pytest

# @pytest.mark.skip
def test_single_1():

    mainexe = MainExecutor()

    mainexe.book_cover_extraction(0, "Img3.png")

    assert mainexe.title.strip() == "ERAGON"
    assert mainexe.pub.strip() == "PENGUIN,"
    assert mainexe.isbn.strip() == "978-0-13-601970-1"

def test_multiple():

    mainexe = MainExecutor()

    mainexe.book_cover_extraction(1, "img_test")

    assert mainexe.title.strip() == "Excellence: Can We Be Equal and Excellent Too?  ERAGON"
    assert mainexe.pub.strip() == "PENGUIN, PENGUIN,"
    assert mainexe.isbn.strip() == "978-0-13-601970-1 978-0-13-601970-1"