import scr as scr

def main():
    with open("Ook.txt") as source:
        
        tokens = scr.tokenize(source.read())
        
        program, jumpTable = scr.parse(tokens)
       
        res = scr.vm(program, jumpTable)
        
        print(res)
        print("sup")

    with open("ascii.txt") as source:
        print(source.read())
        

if __name__ == "__main__":
    main()
