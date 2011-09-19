def conflict(state, nextX):
    '''
    It is true if the horizontal distance between the next queen and the previous one under
    consideration is either zero (same column) or equal to the vertical distance (on a diagonal).
    Otherwise, it is false.
    '''
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY-i):
            return True
    return False

def queens(num, state = ()):
    '''
    It can create a generator for queen's positions for num number of queens
    '''
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyPrint(solution):
    '''
    This will print a solution of a set of queen's positions.
    '''
    def line(pos, length = len(solution)):
        return '. ' * (pos) + 'X ' + '. '* (length-pos-1)
    for pos in solution:
        print line(pos)
        
prettyPrint(queens(8).next()) 