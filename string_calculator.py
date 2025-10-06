class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter, numbers = self._extract_delimiter(numbers)
        numbers = numbers.replace("\n", delimiter)

        parts = self._to_int_list(numbers, delimiter)
        self._raise_if_negatives(parts)

        return sum(x for x in parts if x <= 1000)

    @staticmethod
    def _extract_delimiter(numbers: str):
        """Detect custom or default delimiter."""
        delimiter = ","
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter = header[3:-1] if header.startswith("//[") else header[2]
        return delimiter, numbers

    @staticmethod
    def _to_int_list(numbers: str, delimiter: str):
        """Convert delimited string to integer list."""
        return [int(x) for x in numbers.split(delimiter) if x]

    @staticmethod
    def _raise_if_negatives(parts):
        """Raise error if negative numbers are found."""
        negatives = [x for x in parts if x < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
