# TDD Driven StringCalculator

Build a StringCalculator functionality that can take up to two numbers, separated by commas, and will return their sum. 
for example “” or “1” or “1,2” as inputs.

> DO NOT jump into implementation! Read the example and the starting task below.

- For an empty string it will return 0
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: “1\n2,3” (will equal 6)
  - the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)
- Support different delimiters : to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
the first line is optional. all existing scenarios should still be supported
- Calling Method with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. if there are multiple negatives, show all of them in the exception message.
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2
- Delimiters can be of any length with the following format: “//[delimiter]\n” for example: “//[***]\n1***2***3” should return 6

## Tasks



Establish quality parameters:

- Ensure  maximum complexity (CCN) per function == 3

- Ensure 100% line and branch coverage at every step

  

Start Test-driven approach

1. Write the smallest possible failing test: give input `"" assert output to be 0 ` .
2. Write the minimum amount of code that'll make it pass.
3. Refactor any assumptions, continue to pass this test. Do not add any code without a corresponding test.




## Test specifications based on requirements

---

### 1. **Empty String Returns Zero**
- Input: `""`
- Output: `0`

### 2. **Single Number Returns That Number**
- Input: `"1"`
- Output: `1`

### 3. **Two Numbers, Comma Separated**
- Input: `"1,2"`
- Output: `3`

### 4. **Unknown Amount of Numbers**
- Input: `"1,2,3,4"`
- Output: `10`

### 5. **New Lines as Delimiters**
- Input: `"1\n2,3"`
- Output: `6`

### 6. **Custom Single-Character Delimiter**
- Input: `"//;\n1;2"`
- Output: `3`

### 7. **Custom Multi-Character Delimiter**
- Input: `"//[***]\n1***2***3"`
- Output: `6`

### 8. **Negative Numbers Throw Exception**
- Input: `"1,-2,3"`
- Exception: `"negatives not allowed: -2"`

- Input: `"1,-2,-3"`
- Exception: `"negatives not allowed: -2, -3"`

### 9. **Numbers Greater Than 1000 Are Ignored**
- Input: `"2,1001"`
- Output: `2`

### 10. **Delimiter Format Validation**
- Input: `"1,\n"`
- Output: (Should not be supported; no need to test, just clarifying)

---

This list covers all functional requirements and quality constraints for the StringCalculator TDD process.
