class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","

        # Custom delimiter format
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            if header.startswith("//["):   # multi-character delimiter
                delimiter = header[3:-1]
            else:                          # single-character delimiter
                delimiter = header[2]

        # Normalize newlines into delimiter
        numbers = numbers.replace("\n", delimiter)

        # Split and convert
        parts = [int(x) for x in numbers.split(delimiter) if x]

        # Check negatives
        negatives = [x for x in parts if x < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        # Ignore >1000
        return sum(x for x in parts if x <= 1000)
