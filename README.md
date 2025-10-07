# Programming in Science - Midterm Exam - V1

This template repository is the starter project for the Programming in Science Winter 2025 Midterm Exam V1. Written in Python, and tested with Pytest.


# Instructions
* Internet access and use of AI are not allowed during the exam except the links provided by the teacher.
* Students must submit the exam via GitHub, simply by pushing back to the same repository they cloned this handout.
* The teacher will not answer questions during the exam.
* Students must keep silent during the exam time.
* Phone, laptop, and similar are NOT allowed during the exam.  
* Plagiarism, any attempt at plagiarism or complicity in plagiarism during an evaluation, will result in a course failure. 

### Question(s)


1.  **Write a  function `sum_of_even_nums_in(numbers)` that returns the sum of even numbers in the list of `numbers`.**

#### Example:
   ```python
  sum_of_even_nums_in([5,10,2,8])    # Output: 20
  sum_of_even_nums_in([1,9,10,8])    # Output: 18
  ```


2. **Write a function `area_of_triangle(a, b, c)` that calculates the area of a triangle given the lengths of all three sides using Heron's formula. [ s=(a + b + c)/2,  A = sqrt(s * (s - a) * (s - b) * (s - c)) ] .**
   - The function should return the area rounded to 2 decimal places.
   - Use the sqrt function from the math module if needed.

 #### Example:
   ```python
   
  area_of_triangle(3, 4, 5)    # Output: 6.0
  area_of_triangle(2, 2, 2)    # Output: 1.73
 
   ```

3.  **String reversal: Write a function `reverse_string(s)` that recursively reverse a string `s` by processing the first character and reversing the rest.**

```python
# Example
reverse_string("hello") --> "olleh" 
```
4. **Write a function `hollow_triangle_with_upper_left_right_angle(n)` that returns a string representing a triangle with upper left right angle pattern of star-space (`* `) with height `n`.**
   - The height should be at least 3.

   #### Example (n = 3):
   ```python
   hollow_triangle_with_upper_left_right_angle(3)

   # Output:
   
    * * * 
    * * 
    *
   ```
   #### Example (n = 4):
   ```python
   hollow_triangle_with_upper_left_right_angle(4)

   # Output:
    
    * * * * 
    *   * 
    * * 
    *
   ```


   #### Example (n = 5):
   ```python
   hollow_triangle_with_upper_left_right_angle(5)

   # Output:
   
    * * * * * 
    *     * 
    *   * 
    * * 
    *
   ```

5. **Write a function `rhombus_shape(n)` that returns a string representing a rhombus pattern of star-space (`*`) with height `n`.**
   - The rows should be at least 3.
   
#### Example (n = 3):
```python
   rhombus_shape(3)

### Output:
  *
 ***
*****
 ***
  *
```

#### Example (n = 4):
```python
   rhombus_shape(4)

### Output:
      
   *
  ***
 *****
*******
 *****
  ***
   *
```
#### Example (n = 5):
```python
   rhombus_shape(5)

### Output:
      
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
### Run Command

```
pytest

