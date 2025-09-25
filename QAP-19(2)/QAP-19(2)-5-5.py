tests_run = 0
tests_failed = 0

def test_case_generator():
    case_id = 0

    def run_test(test):
        global tests_run
        tests_run += 1
        global tests_failed
        x = test()
        if not x: tests_failed += 1
        nonlocal case_id
        case_id += 1
        return case_id

    return run_test




