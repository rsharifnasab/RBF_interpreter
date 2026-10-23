#!/usr/bin/env python3

import enum
from collections import defaultdict
from sys import argv

valid_chars = "+-[]><.,$"


def tokenize(content):
    return [c for c in content if c in valid_chars]


class Machine:
    def __init__(self, tokens, init_data):
        self.data_pointer = 0
        self.tokens = tokens
        self.data = defaultdict(int)
        self.pc = 0
        if init_data:
            self.data[0] = init_data
            self.print()

    def __cur(self):
        return self.data[self.data_pointer]

    def increase_dp(self):
        self.data_pointer += 1

    def decrease_dp(self):
        assert self.data_pointer > 0
        self.data_pointer -= 1
        assert self.data_pointer >= 0

    def increment(self):
        self.data[self.data_pointer] = (self.data[self.data_pointer] + 1) % 256

    def decrement(self):
        res = self.data[self.data_pointer] - 1
        if res == -1:
            res = 255
        self.data[self.data_pointer] = res

    def print_char(self):
        print(chr(self.__cur()), end="")

    def input_char(self):
        c = ord(input()[0])
        self.data[self.data_pointer] = c

    def _get_matching_right(self, q):
        assert self.tokens[q] in ["["]
        st = []

        for i, c in enumerate(self.tokens[q:]):
            if c == "[":
                st.append(c)
            elif c == "]":
                st.pop()
                if not st:  # stack is empty
                    return i + q

        assert False

    def _get_matching_left(self, q):
        assert self.tokens[q] in ["]"]
        st = []

        l = list(enumerate(self.tokens))

        for i, c in l[: q + 1][::-1]:
            if c == "]":
                st.append(c)
            elif c == "[":
                st.pop()
                if not st:  # stack is empty
                    return i

        assert False

    # ]
    def jump_left(self):
        if self.__cur() == 0:
            return
        self.pc = self._get_matching_left(self.pc)

    # [
    def jump_right(self):
        if self.__cur() != 0:
            return
        self.pc = self._get_matching_right(self.pc)

    def debug(self):
        print("---debug---")
        self.print()
        print(f"{self.pc=} {self.data_pointer=}")

    def interpret(self):
        while True:
            t = self.tokens[self.pc]
            if t == ">":
                self.increase_dp()
            if t == "<":
                self.decrease_dp()
            if t == "+":
                self.increment()
            if t == "-":
                self.decrement()
            if t == ".":
                self.print_char()
            if t == ",":
                self.input_char()
            if t == "[":
                self.jump_right()
            if t == "]":
                self.jump_left()
            if t == "$":
                self.debug()

            self.pc += 1

            if self.pc >= len(self.tokens):
                print("\ndone")

                return

    def print(self):
        for i in range(20):
            print(self.data[i], end="|")
        print()


def main(args):
    assert len(args) == 2

    with open(args[0]) as f:
        content = f.read()
        tokens = tokenize(content)
        m = Machine(tokens, int(args[1]))
        m.interpret()
        m.print()


if __name__ == "__main__":
    main(argv[1:])


def _test():
    machine = Machine([".", "[", "[", "]", "[", "]", "]", "]"])
    print(machine._get_matching_right(1))  # 6

    print("--")
    print(machine._get_matching_left(6))  # 0
