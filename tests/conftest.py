import pytest

from tinygpt import SimpleTokenizerV1


@pytest.fixture
def vocab() -> dict[str, int]:
    tokens = ["Hello", "world", "how", "are", "you", ",", ".", "?", "--"]
    return {token: index for index, token in enumerate(tokens)}


@pytest.fixture
def tokenizer(vocab: dict[str, int]) -> SimpleTokenizerV1:
    return SimpleTokenizerV1(vocab)
