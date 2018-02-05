print "Running math library unit tests (test_math.py)."

import srcmath as srcmath

a = 5
b = 5

# Test srcAdd
if srcmath.srcAdd(a, b) != 10:
	print "srcAdd failed for " + a + " " + b

# Test srcSubstract
if srcmath.srcSubtract(a, b) != 0:
	print "srcSubtract failed for " + a + " " + b

# Test srcMultiply
if srcmath.srcMultiply(a, b) != 25:
	print "srcMultiply failed for " + a + " " + b

# Test srcDivide
if srcmath.srcDivide(a, b) != 1:
	print "srcDivide failed for " + a + " " + b

print "Finished running math library unit tests."
