def main():
    lines = []
    with open('glossary.qmd') as f:
        for line in f:
            if line.startswith("#### "):
                lines.append(line[5:].strip())

    # Case-insensitive
    lines = [line.lower() for line in lines]

    # Sort
    sorted_lines = sorted(lines)

    for orig, sort in zip(lines, sorted_lines):
        if orig != sort:
            print(f"'{sort}' is out of order; should be before '{orig}'")
            exit(1)

if __name__ == "__main__":
    main()
