import math

def isSmaller(a, b, c, temp):
    if abs(a) + abs(b) + abs(c) + 4 < abs(temp):
        return True
    return False


def generator(program):
    code = []
    ip = 0
    
    for p in program:
        temp = p - ip
    
        if temp == 0:
            code.append("outCell")
        else:
            a = int(math.sqrt(abs(temp)))
            b = temp // a
            c = temp - (a * b)

            if isSmaller(a, b, c, temp):
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

        ip = p
        
    
    return code
