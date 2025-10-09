
def update(score):
    with open('score.txt', 'r') as f:
        t = f.read()
        if score >= int(t):
            with open('score.txt', 'w') as f:
                f.write(str(score))

def show():
    with open('score.txt') as f:
        return f.read()
    