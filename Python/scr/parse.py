def parse(tokens):
    program = []
    jumpTable = {}
    stack = []

    for i in range(0, len(tokens), 2):
        token = tokens[i] + " " + tokens[i+1]
        instrIndex = len(program)

        match token:
            case "Ook. Ook?":
                program.append("ptrRight")
            case "Ook? Ook.":
                program.append("ptrLeft")
            case "Ook. Ook.":
                program.append("incCell")
            case "Ook! Ook!":
                program.append("decCell")
            case "Ook! Ook.":
                program.append("outCell")
            case "Ook. Ook!":
                program.append("inCell")
            case "Ook! Ook?":
                program.append("jmpFwd")
                stack.append(instrIndex)
            case "Ook? Ook!":
                program.append("jmpBck")
                start = stack.pop()
                end = instrIndex
                jumpTable[start] = end
                jumpTable[end] = start
            case _:
                raise ValueError(f"Invalid token pair: {token}")

    return program, jumpTable

def main():
    print("parse")

if __name__=="__main__":
    main()
