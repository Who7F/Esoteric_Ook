import scr as scr

def main():
    
    with open("Ook.txt") as source:
        
        tokens = scr.tokenizeOok(source.read())

        program, jumpTable = scr.parseOok(tokens)

        res = scr.vm(program, jumpTable)
        
        print(res)

    
    with open("ascii.txt") as source:
        
        tokens = scr.tokenizeAscii(source.read())

        program = scr.parseAscii(tokens)

        code = scr.generator(program)

        print(code)
                
        test = scr.encOok(code)

        tokens = scr.tokenizeOok(test)

        program, jumpTable = scr.parseOok(tokens)
       
        res = scr.vm(program, jumpTable)
        
        print(res)
        


if __name__ == "__main__":
    main()
