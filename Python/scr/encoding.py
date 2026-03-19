def encOok(code):
    ook = []

    for c in code:
        match c:
            
            case "ptrRight":
                ook.append("Ook. Ook? ")
            case "ptrLeft":
                ook.append("Ook? Ook. ")
            case "incCell":
                ook.append("Ook. Ook. ")
            case "decCell":
                ook.append("Ook! Ook! ")
            case "outCell":
                ook.append("Ook! Ook. ")
            case "inCell":
                ook.append("Ook. Ook! ")
            case "jmpFwd":
                ook.append("Ook! Ook? ")
            case "jmpBck":
                ook.append("Ook? Ook! ")

            case _:
                raise ValueError(f"Invalid token pair: {c}")

    
    return ''.join(ook)
