# 🐍 Day 2: 10 More Python Problems

## 📌 The Story Behind This File

Day 2. Still here. Still showing up.

Last night I proved I could start. Tonight I proved I could continue.

These problems are harder than Day 1. Loops. Logic. Functions. Palindromes. Prime numbers. Fibonacci.

My brain melted a little. But I Googled. I debugged. I figured it out.

This is what growth looks like — messy, slow, but forward.

---

## 📝 Problems Solved

| # | Problem | What I Learned |
|---|---------|----------------|
| 11 | Sum of first n natural numbers | Math formula: `n*(n+1)/2` — much faster than loops! |
| 12 | Count digits in an integer | `len(str(number))` — converting to string is magical ✨ |
| 13 | Reverse digits of a number | Slicing `[::-1]` — my new favorite trick |
| 14 | Palindrome checker | Works for numbers AND words! Case-insensitive too |
| 15 | Armstrong number | `153 = 1³ + 5³ + 3³` — math is wild |
| 16 | Prime number check | Loops, remainders, and why 2 is special |
| 17a | First 10 Fibonacci numbers | The rabbit sequence! 🐇 |
| 17b | Fibonacci by user input | Made it flexible |
| 18 | Find all factors of a number | Division and remainders again |
| 19 | Vowel or consonant | `isalpha()` saved me from crashing on symbols |
| 20 | ASCII value | `ord()` — letters have secret numbers! |

---

## 🛠️ Concepts Used

- `def` functions (so I don't repeat myself!)
- `return` vs `print` (finally clicked!)
- String slicing `[::-1]` for reversing
- `len()` for counting digits
- `for` loops with `range()`
- `if/elif/else` logic
- `%` modulo operator (my new best friend)
- `isinstance()` to check data types
- `isalpha()` to validate letters
- `ord()` and ASCII values

---

## 🧠 What I Learned

- **Palindromes work on strings AND numbers** — just convert to string!
- **Armstrong numbers care about digit count** — `153` is 3 digits, so cube each digit
- **Prime checking is SLOW if you loop too much** — I'll learn optimization later
- **Fibonacci is just adding two numbers and shifting** — `a, b = b, a + b` is beautiful ✨
- **Factors come in pairs** — I check all numbers up to n, but I learned there's a faster way
- **Vowel checking needs `.isalpha()` first** — otherwise symbols break everything!
- **ASCII is cool** — `ord('A')` = 65, and `chr(65)` = 'A'

---

## 💭 Real Talk

Some of these problems felt impossible at first.

Problem 15 (Armstrong) broke me for 20 minutes because I put the `input()` INSIDE the function. Once I moved it outside — boom. Worked.

Problem 18 (Factors) seemed simple but I kept getting a `NameError` because I used `n` instead of `r`. One letter. 10 minutes of staring.

But every mistake taught me something.

---

## 📸 Proof

Code runs. Outputs are clean. Brain is tired but happy.

---

## 🔗 Connect With My Journey

10 problems every day. Slowly. Consistently.

- **Follow on LinkedIn:** [linkedin.com/in/nayab-nayyer](https://linkedin.com/in/nayab-nayyer)
- **GitHub Profile:** [github.com/nayabnayyer](https://github.com/nayabnayyer)

---

*"The best way to predict the future is to code it."*

— Nayab, Day 2
