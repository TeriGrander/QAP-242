def compare_test_results(expected, actual):
    pairs = list(zip(expected, actual))
    return list(map(lambda x: x[0] == x[1], pairs))


expected_results = ["pass", "fail", "pass", "pass"]
actual_results = ["pass", "pass", "pass", "fail"]

comparison = compare_test_results(expected_results, actual_results)
print(comparison)
# [True, False, True, False]