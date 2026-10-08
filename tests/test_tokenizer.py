import pytest

from tinygpt import SimpleTokenizerV1


def test_reverse_vocab(tokenizer: SimpleTokenizerV1, vocab: dict[str, int]) -> None:
    assert tokenizer.reverse_vocab[0] == "Hello"
    assert len(tokenizer.reverse_vocab) == len(vocab)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello world", [0, 1]),
        ("Hello, world.", [0, 5, 1, 6]),
        ("  Hello\n\tworld  ", [0, 1]),
        ("Hello--world", [0, 8, 1]),
        ("", []),
    ],
    ids=["words", "punctuation", "extra-whitespace", "double-dash", "empty"],
)
def test_encode(tokenizer: SimpleTokenizerV1, text: str, expected: list[int]) -> None:
    assert tokenizer.encode(text) == expected


def test_encode_unknown_token_raises(tokenizer: SimpleTokenizerV1) -> None:
    with pytest.raises(KeyError):
        tokenizer.encode("Goodbye world")


@pytest.mark.parametrize(
    ("ids", "expected"),
    [
        ([0, 5, 1, 6], "Hello, world."),
        ([], ""),
    ],
    ids=["punctuation", "empty"],
)
def test_decode(tokenizer: SimpleTokenizerV1, ids: list[int], expected: str) -> None:
    assert tokenizer.decode(ids) == expected


def test_round_trip(tokenizer: SimpleTokenizerV1) -> None:
    text = "Hello, how are you? Hello world."
    assert tokenizer.decode(tokenizer.encode(text)) == text
