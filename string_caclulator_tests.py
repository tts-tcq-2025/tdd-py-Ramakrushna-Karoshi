class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter, numbers = self._extract_delimiter(numbers)
        parts = self._to_int_list(numbers, delimiter)
        self._raise_if_negatives(parts)
        return self._sum_ignoring_large(parts)

    def _extract_delimiter(self, numbers: str) -> tuple[str, str]:
        """Extract delimiter from string if present."""
        if not numbers.startswith("//"):
            return ",", numbers

        header, numbers = numbers.split("\n", 1)
        if header.startswith("//[") and header.endswith("]"):
            delimiter = header[3:-1]
        else:
            delimiter = header[2:]
        return delimiter, numbers

    def _to_int_list(self, numbers: str, delimiter: str) -> list[int]:
        """Convert number string to list of ints."""
        return [int(x) for x in numbers.replace("\n", delimiter).split(delimiter) if x]

    def _raise_if_negatives(self, parts: list[int]) -> None:
        """Raise error if negative numbers are found."""
        negatives = [x for x in parts if x < 0]
        if negatives:
            msg = f"negatives not allowed: {', '.join(map(str, negatives))}"
            raise ValueError(msg)

    def _sum_ignoring_large(self, parts: list[int]) -> int:
        """Sum numbers ignoring >1000."""
        return sum(x for x in parts if x <= 1000)
