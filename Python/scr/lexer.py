def tokenizeOok(source: str) -> list[str]:
    tokens = source.split()
    
    if len(tokens) % 2 != 0:
        raise ValueError("Invalid Ook program: uneven tokens")
    else:
        print("Okie dokie")

    return tokens

def tokenizeAscii(source: str) -> list[str]:
    return list(source)


