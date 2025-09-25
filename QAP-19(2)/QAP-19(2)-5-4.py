def generate_test_case():
    case_id = 0

    def next_case():
        nonlocal case_id
        case_id += 1
        return case_id

    return next_case