#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4
    for o in dir(hidden_4):
        if o[:2] != "__":
            print(f"{o}")
