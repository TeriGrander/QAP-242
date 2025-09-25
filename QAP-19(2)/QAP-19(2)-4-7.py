def has_failures(lst):
    return any(list(map(lambda x: x == 'fail', lst)))

def all_passed_or_skipped(lst):
    return all(list(map(lambda x: x == 'pass' or x == 'skip', lst)))


test_results = ["pass", "pass", "skip", "fail", "pass"]

print(has_failures(test_results))
# True
print(all_passed_or_skipped(test_results))
# False