from pathlib import Path
from re import split
from urllib.request import urlretrieve

from tokenizer import SimpleTokenizerV1, UNKNOWN_TOKEN, END_OF_TEXT_TOKEN


def main() -> None:
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = Path("data/the-verdict.txt")
    file_path.parent.mkdir(exist_ok=True)
    urlretrieve(url, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    tokens = split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    tokens = [token for token in tokens if token.strip()]
    deduped_tokens = set(tokens)
    sorted_tokens = sorted(deduped_tokens)
    sorted_tokens.extend([END_OF_TEXT_TOKEN, UNKNOWN_TOKEN])
    vocab = {token:index for index, token in enumerate(sorted_tokens)}

    text = """"It's the last he painted, you know," 
       Mrs. Gisburn said with pardonable pride."""
    tokenizer = SimpleTokenizerV1(vocab)
    ids = tokenizer.encode(text)
    print("ids:", ids)
    output_text = tokenizer.decode(ids)
    print("output_text:", output_text)

    print(len(vocab.items()))
    for i, item in enumerate(list(vocab.items())[-5:]):
        print(item)

    text1 = "Hello, do you like tea?"
    text2 = "In the sunlit terraces of the palace."
    text = (" " + END_OF_TEXT_TOKEN + " ").join((text1, text2))
    print(text)

    ids = tokenizer.encode(text)
    print("ids:", ids)
    print(tokenizer.decode(ids))

if __name__ == "__main__":
    main()
