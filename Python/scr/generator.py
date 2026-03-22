import math

def isSmaller(a, b, c, temp):
    if abs(a) + abs(b) + abs(c) + 4 < abs(temp):
        return True
    return False


def generator(program):
    code = []
    curr = 0
    
    for targ in program:
        temp = targ - curr
    
        if temp == 0:
            code.append("outCell")
        else:
            a = int(math.sqrt(abs(temp))) or 1
            b = temp // a
            c = temp - (a * b)

            if a > 1 and isSmaller(a, b, c, temp):
                for _ in range(abs(a)):
                    code.append("incCell" if a > 0 else "decCell")

                code.append("jmpFwd")

                code.append("ptrRight")
                for _ in range(abs(b)):
                    code.append("incCell" if b > 0 else "decCell")

                code.append("ptrLeft")
                code.append("decCell")

                code.append("jmpBck")

                code.append("ptrRight")

                for _ in range(abs(c)):
                    code.append("incCell" if c > 0 else "decCell")


            else:
                for _ in range(abs(temp)):
                    code.append("incCell" if temp > 0 else "decCell")

        code.append("outCell")
        curr = targ
        
    
    return code
