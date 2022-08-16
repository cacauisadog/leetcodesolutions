# https://leetcode.com/problems/ransom-note/


def can_construct(ransom_note: str, magazine: str) -> bool:
    for letter in ransom_note:
        if letter not in magazine:
            return False

        magazine = magazine.replace(letter, "", 1)
    return True


def test_can_construct():
    ransom_note = "a"
    magazine = "b"
    assert can_construct(ransom_note, magazine) is False

    ransom_note = "aa"
    magazine = "ab"
    assert can_construct(ransom_note, magazine) is False

    ransom_note = "aa"
    magazine = "aab"
    assert can_construct(ransom_note, magazine) is True

    print("All tests passed!")


test_can_construct()
