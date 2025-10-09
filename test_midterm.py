# DO NOT CHANGE THIS FILE, OR ZERO MARK WILL BE ASSIGNED.

import unittest
from Midterm import sum_of_even_nums_in, area_of_triangle, pascal, hollow_triangle_with_upper_left_right_angle, rhombus_shape

# ------------------------------------------------------------
# Test Q1: sum_of_even_nums_in
# ------------------------------------------------------------
def test_sum_of_even_nums_in():
    assert sum_of_even_nums_in([5, 10, 2, 8]) == 20
    assert sum_of_even_nums_in([1, 9, 10, 8]) == 18
    assert sum_of_even_nums_in([3, 5, 7]) == 0
    assert sum_of_even_nums_in([2, 4, 6, 8]) == 20

# ------------------------------------------------------------
# Test Q2: area_of_triangle
# ------------------------------------------------------------
def test_area_of_triangle():
    assert area_of_triangle(3, 4, 5) == 6.0
    assert area_of_triangle(2, 2, 2) == 1.73
    assert area_of_triangle(5, 5, 8) == 12.0
    assert area_of_triangle(10, 10, 12) == 48.0

# ------------------------------------------------------------
# Test Q3: pascal
# ------------------------------------------------------------
def test_pascal():
    # Assuming pascal(n, k) returns the full nth row of Pascal’s Triangle
    assert pascal(0, 0) == [1]
    assert pascal(1, 0) == [1, 1]
    assert pascal(2, 0) == [1, 2, 1]
    assert pascal(3, 0) == [1, 3, 3, 1]
    assert pascal(4, 0) == [1, 4, 6, 4, 1]

# ------------------------------------------------------------
# Test Q4: hollow_triangle_with_upper_left_right_angle
# ------------------------------------------------------------
def test_hollow_triangle_with_upper_left_right_angle():
    assert hollow_triangle_with_upper_left_right_angle(3) == "* * * \n* * \n*"
    assert hollow_triangle_with_upper_left_right_angle(4) == "* * * * \n*   * \n* * \n*"
    assert hollow_triangle_with_upper_left_right_angle(5) == "* * * * * \n*     * \n*   * \n* * \n*"

# ------------------------------------------------------------
# Test Q5: rhombus_shape
# ------------------------------------------------------------
def test_rhombus_shape():
    assert rhombus_shape(3) == "  * \n *** \n***** \n *** \n  *"
    assert rhombus_shape(4) == "   * \n  *** \n ***** \n******* \n ***** \n  *** \n   *"
    assert rhombus_shape(5) == "    * \n   *** \n  ***** \n *******\n********* \n ******* \n  ***** \n   *** \n    *"

# ------------------------------------------------------------
# Run all tests
# ------------------------------------------------------------
if __name__ == "__main__":
    test_sum_of_even_nums_in()
    test_area_of_triangle()
    test_pascal()
    test_hollow_triangle_with_upper_left_right_angle()
    test_rhombus_shape()
    print("All tests passed!")
