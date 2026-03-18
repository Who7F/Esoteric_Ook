def vm(program, jumpTable):
    cells = [0] * 8
    ptr = 0
    ip = 0
    res = []
    ENCODE = "ascii"

    
    while ip < len(program):
        cmd = program[ip]
        match cmd:
            case "ptrRight":
                ptr += 1
            case "ptrLeft":
                ptr -= 1
            case "incCell":
                cells[ptr] += 1
            case "decCell":
                cells[ptr] -= 1
            case "outCell":
                temp = cells[ptr]
                res.append(chr(temp))
            case "inCell":
                print("do somthing")
            case "jmpFwd":
                if cells[ptr] == 0:
                    ip = jumpTable[ip] 
            case "jmpBck":
                if cells[ptr] != 0:
                    ip = jumpTable[ip] 
            case _:
                raise ValueError(f"Invalid token pair: {token}")
            
        ip += 1
         
    return ''.join(res)

