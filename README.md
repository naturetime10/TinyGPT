# TinyGPT

A small GPT-style language model built from scratch in Python.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Usage

```sh
uv sync                   # install dependencies
uv run python -m tinygpt  # run the tokenizer demo
uv run pytest             # run tests
```

The demo downloads *The Verdict* into `data/`, builds a vocabulary from it, and
encodes/decodes sample text with `SimpleTokenizerV1`.

## License

[MIT](LICENSE)
