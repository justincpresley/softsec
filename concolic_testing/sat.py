from z3 import *

def main():
    int_var = Int('int_var')
    float_var = Real('float_var') # note: in our context, float_var can have any decimal values after it.
    s = Solver()

    s.add(ToInt(float_var) == 3 * int_var)
    solvable = "YES" if s.check()==sat else "NO"
    m = s.model()
    print(f"Constraints: {s}")
    print("Solving these constraints...")
    print(f"\tsolvable: {solvable}")
    print(f"\tmodel (solution):")
    for d in m.decls():
        print("\t* %s = %s" % (d.name(), m[d]))


    print("\nAdding more constraints...\n")

    s.add(int_var > ToInt(float_var) - 50)
    solvable = "YES" if s.check()==sat else "NO"
    m = s.model()
    print(f"Constraints: {s}")
    print("Solving these constraints...")
    print(f"\tsolvable: {solvable}")
    print(f"\tmodel (solution):")
    for d in m.decls():
        print("\t* %s = %s" % (d.name(), m[d]))

if __name__ == "__main__":
    main()