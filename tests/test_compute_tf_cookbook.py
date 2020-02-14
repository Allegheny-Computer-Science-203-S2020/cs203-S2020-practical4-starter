"""Test to ensure that the functions in the cookbook-style program are correct."""

from termfrequency import compute_tf_cookbook

# TODO: All all of your test cases from a previous assignment,
# aiming to achieve as high of coverage as is possible

# TODO: Make sure that you also complete the following tasks:
# 1. Install and use the two new suggested plugins
# 2. Use Pytest with these additional plugins and observe changes
# 3. Review the "Python Testing with Pytest" book and try to
# use different command-line options to learn how Pytest works
# 4. Search for other Pytest plugins that you think might be
# useful, seeing if you can install and use them on your own
# 5. Report all of your experiences in the reflection file!


def test_read_file_populates_data_0():
    """Checks that the size of the input variable is correct."""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0
