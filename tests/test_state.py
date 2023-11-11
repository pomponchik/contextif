from contextif import state


def test_set_context_and_run_function():
    flag = False
    def function():
        nonlocal flag
        flag = True

    with state:
        state(function)

    assert flag


def test_not_set_context_and_run_function():
    flag = False
    def function():
        nonlocal flag
        flag = True

    state(function)

    assert not flag
