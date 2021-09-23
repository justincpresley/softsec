It is vital to test all modules / sub-modules of a program to ensure that all requirements
are met. In this program, we only have one small module, simpleCalc. To test this, we need to
ensure that functions (add, subtract, multiply, divide) have proper methods for handling every
input possible.

I did this by doing the following, in order for every single function.
    * Random Valid (int/float) Input Testing: This ensures that it will operate successfully under normal conditions.
    * Boundary Testing: This ensures that regardless of the value of the input, we get some response.
    * Garbage Testing: This ensures that our functions are robust. Whatever we throw at it, we get a proper response.

I made sure that we can change the testing in some way according to our needs. For now, you may change the 'times'
variable in our main() function to increase how many operations happen in our Random Valid Input Testing.

How to run: You can run this program by using python3 doing the following - `python3 test.py`


Below is the Output of Running the Test:

```

Testing simpleCalc for add.
        * Randomizing ints 3 times:
          - -7184418203 + -728744707 = -7913162910
          - 6830709715 + -4136494152 = 2694215563
          - -3482027920 + 3978034157 = 496006237
        * Randomizing floats 3 times:
          - -7580291003.059689 + 23483976.975868225 = -7556807026.08382
          - 6618947273.350275 + -486145099.1661167 = 6132802174.184158
          - 8362337525.388969 + 6238107804.625765 = 14600445330.014734
        * Boundary testing:
          - 8712787587.415405 + 0 = 8712787587.415405
          - 0 + -2280907950.2616034 = -2280907950.2616034
          - 0 + 0 = 0
        * Garbage Input (should result in Error):
          - 1702429035.0987911 + [] = unknown (ERROR)
          - {} + 3826570119.5465183 = unknown (ERROR)

Testing simpleCalc for subtract.
        * Randomizing ints 3 times:
          - 8310352666 - 8406751426 = -96398760
          - 9085478421 - 934733122 = 8150745299
          - 9477575992 - -4032316603 = 13509892595
        * Randomizing floats 3 times:
          - -9515449621.816341 - 4388213868.171871 = -13903663489.988213
          - -5680381413.049471 - -1114776033.0585976 = -4565605379.990873
          - 5506925342.300133 - 1545309334.4998417 = 3961616007.800291
        * Boundary testing:
          - 6018651152.648556 - 0 = 6018651152.648556
          - 0 - -8795764906.298124 = 8795764906.298124
          - 0 - 0 = 0
        * Garbage Input (should result in Error):
          - -1767761153.1623192 - [] = unknown (ERROR)
          - {} - -3348116729.961585 = unknown (ERROR)

Testing simpleCalc for multiply.
        * Randomizing ints 3 times:
          - -3257318643 * 8124447275 = -26463913572928047825
          - 2762847199 * 2357957163 = 6514675343156536437
          - 8915246537 * -3278464778 = -29228321758740973786
        * Randomizing floats 3 times:
          - 3593391251.1164646 * -548335021.4026699 = -1.9703822685891133e+18
          - 1689458859.628477 * -1737563213.9922523 = -2.935541566043742e+18
          - 4024496102.6747932 * -5917240946.533404 = -2.381391312791139e+19
        * Boundary testing:
          - -7157983949.334956 * 0 = -0.0
          - 0 * -2629557722.8752136 = -0.0
          - 0 * 0 = 0
        * Garbage Input (should result in Error):
          - 4137310307.0233765 * [] = unknown (ERROR)
          - {} * 5995425235.224218 = unknown (ERROR)

Testing simpleCalc for divide.
        * Randomizing ints 3 times:
          - 6250131936 / 7549793582 = (q,r): (0, 6250131936)
          - -4506959334 / -4589369746 = (q,r): (0, -4506959334)
          - 7358844692 / 572564708 = (q,r): (12, 488068196)
        * Randomizing floats 3 times:
          - -7260586657.9493885 / -3597642403.9408836 = (q,r): (2.0, -65301850.06762123)
          - 3456691515.505274 / -5834713871.133499 = (q,r): (-1.0, -2378022355.6282253)
          - 5434766554.356285 / -7404338567.830075 = (q,r): (-1.0, -1969572013.4737902)
        * Boundary testing (should result in error if divisor is 0):
          - -3677959383.453368 / 0 = (q,r): unknown (ERROR)
          - 0 / 3242232022.7281246 = (q,r): (0.0, 0.0)
          - 0 / 0 = (q,r): unknown (ERROR)
        * Garbage Input (should result in Error):
          - -2531627916.1913815 / [] = (q,r): unknown (ERROR)
          - {} / -23855194.29123497 = (q,r): unknown (ERROR)


** ALL TESTS PASSED**
simpleCalc is a usable simple calculator with no detected malformities other than the expected!

```