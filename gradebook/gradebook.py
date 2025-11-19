# gradebook/gradebook.py
"""
Gradebook utility functions for operting grades (computing, sorting, etc.).
"""


def average(scores):
    """Compute the average of a list of scores."""
    return sum(scores) / len(scores) if scores else 0.0


def curve(scores, points):
    """Return a new list of scores after adding `points` to each."""
    return [s + points for s in scores]
def median(values):
    """
    Return the median of a list of numeric values.
    If the list is empty, return 0.0
    """
    values = sorted(values)
    n = len(values)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 1:
        return values[mid]
    else:
        return (values[mid - 1] + values[mid]) / 2
def letter_grade(score):
    """Return a letter grade (A, B, C, D, F) for a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
