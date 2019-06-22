try:
    print 6 / 0

except ZeroDivisionError:
    pass

except EnvironmentError:
    print "env error"

else:
    print "no error"

finally:
    # program finally come to here
    print "finally come to here"
