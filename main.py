"""Fridge Roast: one line, biggest laugh.

Writes a single original roast of a smart fridge to /output/entry.txt.
"""
import os

ROAST = (
    "My smart fridge updated its firmware overnight, and now the ice maker "
    "withholds cubes until I give the update five stars."
)


def main():
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
