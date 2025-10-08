Perfect! Here's a **fully polished, visual, Markdown-friendly version** of your README, with tables for clarity, consistent formatting, and clean code blocks. This version will look very professional in GitHub.

---

# 🧪 Programming in Science – Midterm Exam (Winter 2025, V1)

This repository is the **starter project** for the **Programming in Science Midterm Exam (Winter 2025, V1)**.

* **Language:** Python
* **Testing:** Pytest

---

## 📋 Instructions

| Rule                   | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| **Internet & AI**      | Not allowed, except for links explicitly provided by the teacher.       |
| **Submission**         | Push your work to the **same repository** you cloned from this handout. |
| **Questions**          | Teacher will **not answer questions** during the exam.                  |
| **Conduct**            | Maintain **silence** during the exam.                                   |
| **Devices**            | Phone, laptop, and similar devices are **not allowed**.                 |
| **Academic Integrity** | Plagiarism or attempts to cheat will result in **course failure**.      |

---

## 📝 Questions

### 1️⃣ Sum of Even Numbers

**Function:** `sum_of_even_nums_in(numbers)`
**Description:** Returns the sum of all even numbers in the given list `numbers`.

| Input           | Output |
| --------------- | ------ |
| `[5, 10, 2, 8]` | `20`   |
| `[1, 9, 10, 8]` | `18`   |

```python
def sum_of_even_nums_in(numbers):
    ...
```

---

### 2️⃣ Area of a Triangle

**Function:** `area_of_triangle(a, b, c)`
**Description:** Calculates the area using **Heron’s formula**:

$$
s = \frac{a+b+c}{2}, \quad A = \sqrt{s(s-a)(s-b)(s-c)}
$$

* Returns area rounded to **2 decimal places**.
* Use `sqrt` from Python’s `math` module.

| Input       | Output |
| ----------- | ------ |
| `(3, 4, 5)` | `6.0`  |
| `(2, 2, 2)` | `1.73` |

```python
def area_of_triangle(a, b, c):
    ...
```

---

### 3️⃣ Recursive Definition (Pascal’s Rule)

**Function:** `reverse_string(s)`
**Description:** Recursively reverses the string `s`.

| Input      | Output     |
| ---------- | ---------- |
| `"hello"`  | `"olleh"`  |
| `"Python"` | `"nohtyP"` |

```python
def reverse_string(s):
    ...
```

---

### 4️⃣ Hollow Triangle (Upper Left Right Angle)

**Function:** `hollow_triangle_with_upper_left_right_angle(n)`
**Description:** Returns a **hollow triangle** pattern with height `n` using `*`.

* Minimum height: 3

| n | Pattern                                                  |
| - | -------------------------------------------------------- |
| 3 | <pre>\* \* *<br>* *<br>*</pre>                           |
| 4 | <pre>\* \* \* *<br>*   *<br>* *<br>*</pre>               |
| 5 | <pre>\* \* \* \* *<br>*     *<br>*   *<br>* *<br>*</pre> |

```python
def hollow_triangle_with_upper_left_right_angle(n):
    ...
```

---

### 5️⃣ Rhombus Shape

**Function:** `rhombus_shape(n)`
**Description:** Returns a **rhombus** pattern of `*` with height `n`.

* Minimum height: 3

| n | Pattern                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 3 | <pre>  \*<br> ***<br>***\*\*<br> \*\*\*<br>  \*</pre>                                                                                     |
| 4 | <pre>   \*<br>  \***<br> \*\*\*\*\*<br>**\*\*\*\*\*<br> \*\*\*\*\*<br>  \*\*\*<br>   \*</pre>                                             |
| 5 | <pre>    \*<br>   \***<br>  \*\*\*\*\*<br> \*\*\*\*\***<br>****\*\*\*\*\*<br> \*\*\*\*\*\*\*<br>  \*\*\*\*\*<br>   \*\*\*<br>    \*</pre> |

```python
def rhombus_shape(n):
    ...
```

---

## ▶️ Run Tests

```bash
pytest
```

---

✅ This version is **GitHub-ready**, easy to read, and visually structured.

If you like, I can also **add a table of contents with clickable links to each question** at the top, which is great for long READMEs.

Do you want me to add that too?
