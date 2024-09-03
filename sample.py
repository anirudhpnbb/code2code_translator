a = "python\ndef calculate_factorial(num):\n    if num <= 1:\n        return 1\n    else:\n        return num * calculate_factorial(num - 1)\n\nnumber = int(input(\"Enter a number to calculate its factorial:\\n\"))\nfactorial = calculate_factorial(number)\n\nprint(f\"The factorial of {number} is {factorial}\")\n"

print(a)