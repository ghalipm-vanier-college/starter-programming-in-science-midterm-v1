
---

# Programming in Science – Midterm Exam (Fall 2025, V1)

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

### 3️⃣ Pascal’s Rule

**Function:** the n-th row of Pascal’s triangle `pascal(n,k)`

<!--  Each value in Pascal’s triangle (row n, position k) is the sum of the two values directly above it — one from the previous row and previous column, and one from the previous row and same column.
The first and last values in each row are always 1. -->

**Description:** Each row in the triangle satisfies:
`pascal(n,k) = pascal(n-1,k-1) + pascal(n-1,k), 1 ≤ n, 0 ≤ k ≤ n; pascal(n,0) = pascal(n,n) = 1`

```python
| Input (n) | Output (n-th row of Pascal’s Triangle) |
| :-------: | :------------------------------------: |
|     0     |                   [1]                  |
|     1     |                 [1, 1]                 |
|     2     |                [1, 2, 1]               |
|     3     |              [1, 3, 3, 1]              |
|     4     |             [1, 4, 6, 4, 1]            |

```
--- 

```python
def pascal(n,k):
    ...
```

---

### 4️⃣ Hollow Triangle (Upper Left Right Angle)

**Function:** `hollow_triangle_with_upper_left_right_angle(n)`
**Description:** Returns a **hollow triangle** pattern with height `n` using `* `.

* Minimum height: 3

```python

n=3:

* * *
* *
*

n=4:

* * * *
*   *
* *
*
n=5:

* * * * *
*     *
*   *
* * 
*
```

---

```python
def hollow_triangle_with_upper_left_right_angle(n):
    ...
```

---

### 5️⃣ Rhombus Shape

**Function:** `rhombus_shape(n)`
**Description:** Returns a **rhombus** pattern of `*` with height `n`.

* Minimum height: 3

# rhombus shape
```python
n=3:

  *
 ***
*****
 ***
  *
  
 n=4:
 
   *
  ***
 *****
*******
 *****
  ***
   *

 n=5:
 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```
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


