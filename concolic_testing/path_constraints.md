1.
concrete values: float_var=4.4, int_var=10, res=[], temp_var=4
constraints: int(float_var) == 3 * int_var
line found: 3,4

2.
concrete values: float_var=3.4, int_var=1, res=[], temp_var=3
constraints: int_var > int(float_var) - 50
line found: 5

3.
concrete values: float_var=60.5, int_var=20, res=[], temp_var=60
constraints: none, will get the program execution to stop at print(res[5])
line found: 6