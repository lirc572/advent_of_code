import sys

def interpret(pc):
    global mem
    opcode = mem[pc]
    if opcode == 1:
        mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
        return 1
    elif opcode == 2:
        mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
        return 2
    elif opcode == 99:
        return 0
    else:
        return -1

def main():
    global mem, PC
    arguments = sys.argv[1:]
    if not arguments:
        return 1
    if '.' in arguments[0]:
        with open(arguments[0]) as f:
            mem = f.read()
    elif ',' in arguments[0]:
        mem = arguments[0]
    mem = list(map(int, mem.split(',')))
    if len(arguments) == 3:
        mem[1] = int(arguments[1])
        mem[2] = int(arguments[2])
    elif len(arguments) == 2 and len(arguments[1]) == 4:
        mem[1] = int(arguments[1][:2])
        mem[2] = int(arguments[1][2:])
    PC = 0
    while True:
        if interpret(PC):
            PC += 4
        else:
            break
if __name__ == '__main__':
    main()