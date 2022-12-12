
class CathodeRayTube:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.signal = 0
        self.screen = []

    def noop(self):
        self.screen.append("") if self.cycle % 40 == 0 else None
        self.screen[-1] += "#" if self.x - 1 <= self.cycle % 40 <= self.x + 1 else "."
        self.cycle += 1
        x = self.signal
        self.signal += self.cycle * self.x if (self.cycle - 20) % 40 == 0 else 0
        if x != self.signal :
           print("signal", self.cycle, self.x, self.cycle * self.x) 

    def addx(self, i, val):
        for _ in range(2):
            self.noop()
            print(i, self.x)
        self.x += val

    def execute(self, file):
        i = 1 
        with open(file) as fp:
            for line in fp:
                cmd = line.rstrip().split()
                if cmd[0] == "noop":
                    self.noop()
                    print(i, self.x)
                    i += 1 
                elif cmd[0] == "addx":
                    self.addx(i, int(cmd[1]))
                    i += 1
                    print(i, self.x)
                    i += 1

    def show(self):
        return "\n".join(self.screen)


def main():
    crt = CathodeRayTube()
    crt.execute("in")
    print("Part 1:", crt.signal, "\nPart 2:")
    print(crt.show())


if __name__ == "__main__":
    main()


