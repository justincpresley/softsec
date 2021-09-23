from simpleCalc import *
from random import *

def test_add(times):
    print("Testing simpleCalc for add.")
    print(f"\t* Randomizing ints {times} times:")
    for i in range(times):
        val1 = randint(-10**10, 10**10)
        val2 = randint(-10**10, 10**10)
        try:
            print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
        except:
            print(f"\t  - {val1} + {val2} = unknown (ERROR)")
            return False
    print(f"\t* Randomizing floats {times} times:")
    for i in range(times):
        val1 = uniform(-10**10, 10**10)
        val2 = uniform(-10**10, 10**10)
        try:
            print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
        except:
            print(f"\t  - {val1} + {val2} = unknown (ERROR)")
            return False
    print("\t* Boundary testing:")
    val1 = uniform(-10**10, 10**10)
    val2 = 0
    try:
        print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
    except:
        print(f"\t  - {val1} + {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
    except:
        print(f"\t  - {val1} + {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = 0
    try:
        print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
    except:
        print(f"\t  - {val1} + {val2} = unknown (ERROR)")
        return False
    print("\t* Garbage Input (should result in Error):")
    val1 = uniform(-10**10, 10**10)
    val2 = []
    try:
        print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} + {val2} = unknown (ERROR)")
    val1 = {}
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} + {val2} = {simpleCalc.add(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} + {val2} = unknown (ERROR)")
    print()
    return True

def test_subtract(times):
    print("Testing simpleCalc for subtract.")
    print(f"\t* Randomizing ints {times} times:")
    for i in range(times):
        val1 = randint(-10**10, 10**10)
        val2 = randint(-10**10, 10**10)
        try:
            print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
        except:
            print(f"\t  - {val1} - {val2} = unknown (ERROR)")
            return False
    print(f"\t* Randomizing floats {times} times:")
    for i in range(times):
        val1 = uniform(-10**10, 10**10)
        val2 = uniform(-10**10, 10**10)
        try:
            print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
        except:
            print(f"\t  - {val1} - {val2} = unknown (ERROR)")
            return False
    print("\t* Boundary testing:")
    val1 = uniform(-10**10, 10**10)
    val2 = 0
    try:
        print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
    except:
        print(f"\t  - {val1} - {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
    except:
        print(f"\t  - {val1} - {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = 0
    try:
        print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
    except:
        print(f"\t  - {val1} - {val2} = unknown (ERROR)")
        return False
    print("\t* Garbage Input (should result in Error):")
    val1 = uniform(-10**10, 10**10)
    val2 = []
    try:
        print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} - {val2} = unknown (ERROR)")
    val1 = {}
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} - {val2} = {simpleCalc.subtract(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} - {val2} = unknown (ERROR)")
    print()
    return True

def test_multipy(times):
    print("Testing simpleCalc for multiply.")
    print(f"\t* Randomizing ints {times} times:")
    for i in range(times):
        val1 = randint(-10**10, 10**10)
        val2 = randint(-10**10, 10**10)
        try:
            print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
        except:
            print(f"\t  - {val1} * {val2} = unknown (ERROR)")
            return False
    print(f"\t* Randomizing floats {times} times:")
    for i in range(times):
        val1 = uniform(-10**10, 10**10)
        val2 = uniform(-10**10, 10**10)
        try:
            print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
        except:
            print(f"\t  - {val1} * {val2} = unknown (ERROR)")
            return False
    print("\t* Boundary testing:")
    val1 = uniform(-10**10, 10**10)
    val2 = 0
    try:
        print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
    except:
        print(f"\t  - {val1} * {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
    except:
        print(f"\t  - {val1} * {val2} = unknown (ERROR)")
        return False
    val1 = 0
    val2 = 0
    try:
        print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
    except:
        print(f"\t  - {val1} * {val2} = unknown (ERROR)")
        return False
    print("\t* Garbage Input (should result in Error):")
    val1 = uniform(-10**10, 10**10)
    val2 = []
    try:
        print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} * {val2} = unknown (ERROR)")
    val1 = {}
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} * {val2} = {simpleCalc.multiply(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} * {val2} = unknown (ERROR)")
    print()
    return True

def test_divide(times):
    print("Testing simpleCalc for divide.")
    print(f"\t* Randomizing ints {times} times:")
    for i in range(times):
        val1 = randint(-10**10, 10**10)
        val2 = randint(-10**10, 10**10)
        try:
            print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        except:
            print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
            return False
    print(f"\t* Randomizing floats {times} times:")
    for i in range(times):
        val1 = uniform(-10**10, 10**10)
        val2 = uniform(-10**10, 10**10)
        try:
            print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        except:
            print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
            return False
    print("\t* Boundary testing (should result in error if divisor is 0):")
    val1 = uniform(-10**10, 10**10)
    val2 = 0
    try:
        print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
    val1 = 0
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
    except:
        print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
        return False
    val1 = 0
    val2 = 0
    try:
        print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
    print("\t* Garbage Input (should result in Error):")
    val1 = uniform(-10**10, 10**10)
    val2 = []
    try:
        print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
    val1 = {}
    val2 = uniform(-10**10, 10**10)
    try:
        print(f"\t  - {val1} / {val2} = (q,r): {simpleCalc.divide(val1,val2)}")
        return False
    except:
        print(f"\t  - {val1} / {val2} = (q,r): unknown (ERROR)")
    print()
    return True

def check_status(status, prompt):
    if status:
        return
    print(prompt)
    exit()

def main():
    times = 3
    status = test_add(3)
    check_status(status, "simpleCalc did not pass the test for add!")
    status = test_subtract(3)
    check_status(status, "simpleCalc did not pass the test for subtract!")
    status = test_multipy(3)
    check_status(status, "simpleCalc did not pass the test for multiply!")
    status = test_divide(3)
    check_status(status, "simpleCalc did not pass the test for divide!")

    print()
    print("** ALL TESTS PASSED**")
    print("simpleCalc is a usable simple calculator with no detected malformities other than the expected!")

if __name__ == "__main__":
    main()
