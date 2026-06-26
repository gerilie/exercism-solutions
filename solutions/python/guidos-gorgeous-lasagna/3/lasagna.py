"""
Lasagna baking time calculator.
Constants: EXPECTED_BAKE_TIME (40 min), PREPARATION_TIME (2 min/layer).
Functions: bake_time_remaining, preparation_time_in_minutes, elapsed_time_in_minutes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time (EXPECTED_BAKE_TIME - elapsed)."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return total prep time (layers * PREPARATION_TIME)."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed time (prep + bake so far)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
