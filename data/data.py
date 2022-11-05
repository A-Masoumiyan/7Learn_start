from datetime import datetime


def announce(name, age, scores):
    print(f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
    passed = 0
    for score in scores:
        if score >= 12:
            passed += 1
    return f'{name} ({age}), passed {passed} courses.'
