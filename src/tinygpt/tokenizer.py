from re import split, sub

UNKNOWN_TOKEN = "<|unknown|>"
END_OF_TEXT_TOKEN = "<|endoftext|>"

class SimpleTokenizerV1:
    def __init__(self, vocab: dict[str, int]) -> None:
        self.vocab: dict[str, int] = vocab
        self.reverse_vocab: dict[int, str] = {index:token for token, index in vocab.items()}

    def encode(self, text: str) -> list[int]:
        tokens = split(r'([,.:;?_!"()\']|--|\s)', text)
        tokens = [token for token in tokens if token.strip()]
        tokens = [token if token in self.vocab else UNKNOWN_TOKEN for token in tokens]
        ids = [self.vocab[token] for token in tokens]
        return ids

    def decode(self, ids: list[int]) -> str:
        tokens = [self.reverse_vocab[id] for id in ids]
        text = " ".join(tokens)
        text = sub(r' ([,.:;?_!"()\']|--)', r'\1', text)
        return text
