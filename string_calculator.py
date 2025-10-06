class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter, numbers = self._extract_delimiter(numbers)
        parts = self._parse_numbers(numbers, delimiter)
        self._check_negatives(parts)
        return self._sum_ignoring_large(parts)

    def _extract_delimiter(self, text: str) -> tuple[str, str]:
        """Extract the delimiter (single or multi-character) if defined."""
        if not text.startswith("//"):
            return ",", text

        header, text = text.split("\n", 1)
        if header.startswith("//[") and header.endswith("]"):
            return header[3:-1], text
        return header[2:], text

    def _parse_numbers(self, text: str, delimiter: str) -> list[int]:
        """Replace newlines, split, and convert to integers."""
        return [int(x) for x in text.replace("\n", delimiter).split(delimiter) if x]

    def _check_negatives(self, numbers: list[int]) -> None:
        """Raise error if negative numbers are found."""
        negatives = [n for n in numbers if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

    def _sum_ignoring_large(self, numbers: list[int]) -> int:
        """Sum numbers ignoring those > 1000."""
        return sum(n for n in numbers if n <= 1000)
