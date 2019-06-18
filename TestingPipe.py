import os, sys


r, w = os.pipe()

pid = os.fork()

# parent process
if pid:
    os.close(w)
    r = os.fdopen(r)
    for i in range(0,60):
        received = r.read()
        print("{} : signed, parent {}\n".format(received, i))
    sys.exit(0)
# child process
else:
    os.close(r)
    w = os.fdopen(w,'w')
    for i in range(0,31):
        w.write("{}. This is from child\n".format(i))
    sys.exit(0)
