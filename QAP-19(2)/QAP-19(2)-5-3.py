import random

tests_run = 0
tests_failed = 0

def run_test(test):
    # Представим, что test — это функция, которая возвращает True, если тест прошёл, и False в противном случае
    global tests_run
    tests_run += 1
    global tests_failed
    x = test()
    if not x: tests_failed += 1

def test():
    x = random.randint(1, 10)
    return (x % 2 == 0)

run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')
run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')
run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')
run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')
run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')
run_test(test)
print(f'Tests run: {tests_run}, failed: {tests_failed}')