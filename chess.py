from colorama import Fore

# L'idea è quella di definire le mosse dei vari pezzi come liste o insiemi di posizioni
def pos_rebianco(board):
    state = False
    y = 0
    x = 0
    for i in range(len(board)):
        if state == True:
            break
        else:
            y = y + 1
            x = 0
            for j in range(len(board[i])):
                x = x + 1
                if board[i][j] == "Rb":
                    state = True
                    break

    if state == True:

        pos = [asse_y[y], asse_x[x - 1]]
        return pos
    else:

        return None


def pos_rerosso(board):

        state = False
        y = 0
        x = 0
        for i in range(len(board)):
            if state == True:
                break
            else:
                y = y + 1
                x = 0
                for j in range(len(board[i])):
                    x = x + 1
                    if board[i][j] == "Rr":
                        state = True
                        break
        if state == True:
            pos = [asse_y[y],asse_x[x - 1]]
            return pos
        else:

            return None


def Move_set(board,posizi) :

    moves = []
    pos = []
    pos.append(int(posizi[0]))
    pos.append(posizi[1])
    if board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "tb":
        f = 0
        for i in range(7):
            f += 1
            prima = int(pos[0]) - f
            if board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_rossi:
                moves.append([prima, pos[1]])
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_bianchi:
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] == "00":
                moves.append([prima, pos[1]])
        f = 0
        for i in range(7):
            f += 1
            prima = int(pos[0]) + f
            if board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_rossi:
                moves.append([prima, pos[1]])
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_bianchi:
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] == "00":
                moves.append([prima, pos[1]])
        f = 0
        for i in range(7):
            try:
                f += 1
                indice = asse_x.index(pos[1])
                prima = indice + f
                prima = asse_x[prima]
                if board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_rossi:
                    moves.append([pos[0], prima])
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_bianchi:
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] == "00":
                    moves.append([pos[0], prima])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                indice = asse_x.index(pos[1])
                prima = indice - f
                if prima < 0:
                    break
                prima = asse_x[prima]
                if board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_rossi:
                    moves.append([pos[0], prima])
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_bianchi:
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] == "00":
                    moves.append([pos[0], prima])
            except IndexError:
                moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "tr":
        f = 0
        for i in range(7):
            f += 1
            prima = int(pos[0]) - f
            if board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_rossi:

                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_bianchi:
                moves.append([prima, pos[1]])
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] == "00":
                moves.append([prima, pos[1]])
        f = 0
        for i in range(7):
            f += 1
            prima = int(pos[0]) + f
            if board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_rossi:

                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] in pezzi_bianchi:
                moves.append([prima, pos[1]])
                break
            elif board[assey_pos[prima]][assex_ps[pos[1]]] == "00":
                moves.append([prima, pos[1]])
        f = 0
        for i in range(7):
            try:
                f += 1
                indice = asse_x.index(pos[1])
                prima = indice + f
                prima = asse_x[prima]
                if board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_rossi:

                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_bianchi:
                    moves.append([pos[0], prima])
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] == "00":
                    moves.append([pos[0], prima])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                indice = asse_x.index(pos[1])
                prima = indice - f
                if prima < 0:
                    break
                prima = asse_x[prima]
                if board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_rossi:

                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] in pezzi_bianchi:
                    moves.append([pos[0], prima])
                    break
                elif board[assey_pos[pos[0]]][assex_ps[prima]] == "00":
                    moves.append([pos[0], prima])
            except IndexError:
                moves = moves

    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "ab":
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] + f
                if board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y],asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] -f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "ar":
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] + f
                if board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "rb":

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] + f
                if board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])]
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])]
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]]
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]]
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] in pezzi_bianchi:
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "rr":

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] + f
                if board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves

        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])]
                x = assex_ps[pos[1]] + f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])]
                x = assex_ps[pos[1]] - f
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] - f
                x = assex_ps[pos[1]]
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves
        f = 0
        for i in range(7):
            try:
                f += 1
                y = assey_pos[int(pos[0])] + f
                x = assex_ps[pos[1]]
                if x < 0 or y < 0:
                    break
                elif board[y][x] in pezzi_rossi:

                    break
                elif board[y][x] in pezzi_bianchi:
                    moves.append([asse2_y[y], asse_x[x]])
                    break
                elif board[y][x] == "00":
                    moves.append([asse2_y[y], asse_x[x]])
            except IndexError:
                moves = moves

    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "cb":
        for i in range(2):

            if i == 0:
                f = 2
            else:
                f = -2
            for j in range(2):
                s = 1

                if j == 0:

                    try:
                        y = assey_pos[int(pos[0])] - f
                        x = assex_ps[pos[1]] + s
                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] in pezzi_bianchi:
                             moves = moves

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
                else:

                    try:
                        y = assey_pos[int(pos[0])] - f
                        x = assex_ps[pos[1]] - s

                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] in pezzi_bianchi:
                            moves = moves

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
        for i in range(2):

            if i == 0:
                f = 2
            else:
                f = -2
            for j in range(2):
                s = 1

                if j == 0:

                    try:
                        y = assey_pos[int(pos[0])] + s
                        x = assex_ps[pos[1]] + f
                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] in pezzi_bianchi:
                             moves = moves

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
                else:

                    try:
                        y = assey_pos[int(pos[0])] - s
                        x = assex_ps[pos[1]] + f

                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] in pezzi_bianchi:
                            moves = moves

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "cr":
        for i in range(2):

            if i == 0:
                f = 2
            else:
                f = -2
            for j in range(2):
                s = 1

                if j == 0:

                    try:
                        y = assey_pos[int(pos[0])] - f
                        x = assex_ps[pos[1]] + s
                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves = moves

                        elif board[y][x] in pezzi_bianchi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
                else:

                    try:
                        y = assey_pos[int(pos[0])] - f
                        x = assex_ps[pos[1]] - s

                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves = moves

                        elif board[y][x] in pezzi_bianchi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
        for i in range(2):

            if i == 0:
                f = 2
            else:
                f = -2
            for j in range(2):
                s = 1

                if j == 0:

                    try:
                        y = assey_pos[int(pos[0])] + s
                        x = assex_ps[pos[1]] + f
                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves = moves

                        elif board[y][x] in pezzi_bianchi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
                else:

                    try:
                        y = assey_pos[int(pos[0])] - s
                        x = assex_ps[pos[1]] + f

                        if x < 0 or y < 0:
                            moves = moves
                        elif board[y][x] in pezzi_rossi:
                            moves = moves

                        elif board[y][x] in pezzi_bianchi:
                            moves.append([asse2_y[y], asse_x[x]])

                        elif board[y][x] == "00":
                            moves.append([asse2_y[y], asse_x[x]])
                    except IndexError:
                        moves = moves
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "pb":
        y = assey_pos[int(pos[0])]
        x = assex_ps[pos[1]]
        if y == 6:
            if board[y - 1][x] == "00":
                moves.append([asse2_y[y - 1], asse_x[x]])
                if board[y - 2][x] == "00":
                    moves.append([asse2_y[y - 2], asse_x[x]])
            moves = moves
            if board[y - 1][x + 1] in pezzi_rossi:
                moves.append([asse2_y[y - 1], asse_x[x + 1]])
            moves = moves
            if board[y - 1][x - 1] in pezzi_rossi:
                moves.append([asse2_y[y - 1], asse_x[x - 1]])
        else:

            if board[y - 1][x] == "00":
                moves.append([asse2_y[y - 1], asse_x[x]])
            moves = moves
            if board[y - 1][x + 1] in pezzi_rossi:
                moves.append([asse2_y[y - 1], asse_x[x + 1]])
            moves = moves
            if board[y - 1][x - 1] in pezzi_rossi:
                moves.append([asse2_y[y - 1], asse_x[x - 1]])
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "pr":
        y = assey_pos[int(pos[0])]
        x = assex_ps[pos[1]]
        if y == 1:
            if board[y + 1][x] == "00":
                moves.append([asse2_y[y + 1], asse_x[x]])
                if board[y + 2][x] == "00":
                    moves.append([asse2_y[y + 2], asse_x[x]])
            moves = moves
            if board[y + 1][x + 1] in pezzi_bianchi:
                moves.append([asse2_y[y + 1], asse_x[x + 1]])
            moves = moves
            if board[y + 1][x - 1] in pezzi_bianchi:
                moves.append([asse2_y[y + 1], asse_x[x - 1]])
        else:

            if board[y + 1][x] == "00":
                moves.append([asse2_y[y + 1], asse_x[x]])
            moves = moves
            if board[y + 1][x + 1] in pezzi_rossi:
                moves.append([asse2_y[y + 1], asse_x[x + 1]])
            moves = moves
            if board[y + 1][x - 1] in pezzi_rossi:
                moves.append([asse2_y[y + 1], asse_x[x - 1]])
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "Rb":
        y = assey_pos[int(pos[0])]
        x = assex_ps[pos[1]]
        for i in range(3):
            if i == 0:
                f = 0
            elif i == 1:
                f = + 1
            elif i == 2:
                f = -1
            for j in range(3):
                if j == 0:
                    s = 0
                elif j == 1:
                    s = 1
                elif j == 2:
                    s = -1
                moves = moves
                if board[y+f][x+s] in pezzi_rossi:
                    moves.append([asse2_y[y+f], asse_x[x+s]])
                elif board[y+f][x+s] == "00":
                    moves.append([asse2_y[y+f], asse_x[x+s]])
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "Rr":
        y = assey_pos[int(pos[0])]
        x = assex_ps[pos[1]]
        for i in range(3):
            if i == 0:
                f = 0
            elif i == 1:
                f = + 1
            elif i == 2:
                f = -1
            for j in range(3):
                if j == 0:
                    s = 0
                elif j == 1:
                    s = 1
                elif j == 2:
                    s = -1
                moves = moves
                if board[y + f][x + s] in pezzi_bianchi:
                    moves.append([asse2_y[y + f], asse_x[x + s]])
                elif board[y + f][x + s] == "00":
                    moves.append([asse2_y[y + f], asse_x[x + s]])
    elif board[assey_pos[int(pos[0])]][assex_ps[pos[1]]] == "00":
        return None

    return moves

asse_x = ["a","b","c","d","e","f","g","h"]
asse_y = {1:8,2:7,3:6,4:5,5:4,6:3,7:2,8:1}
assex_ps = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
assey_pos = {8:0,7:1,6:2,5:3,4:4,3:5,2:6,1:7}
asse2_y = {0:8,1:7,2:6,3:5,4:4,5:3,6:2,7:1}


Rebianco = True
Rerosso = True


game_board = [

    ["tr", "cr", "ar", "Rr", "rr", "ar", "cr", "tr"],
    ["pr", "pr", "pr", "pr", "pr", "pr", "pr", "pr"],
    ["00", "00", "00", "00", "00", "00", "00", "00"],
    ["00", "00", "00", "00", "00", "00", "00", "00"],
    ["00", "00", "00", "00", "00", "00", "00", "00"],
    ["00", "00", "00", "00", "00", "00", "00", "00"],
    ["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
    ["tb", "cb", "ab", "rb", "Rb", "ab", "cb", "tb"]
]

pedone_bianco = "pb"
pedone_rosso = "pr"
torre_bianca = "tb"
torre_rossa = "tr"
alfiere_bianco = "ab"
alfiere_rosso = "ar"
regina_bianca = "rb"
regina_rossa = "rr"
re_bianco = "Rb"
re_rosso = "Rr"
cavallo_bianco = "cb"
cavallo_rosso = "cr"

pezzi_bianchi = ["pb","Rb","cb","tb","rb","ab"]
pezzi_rossi = ["pr","Rr","cr","tr","rr","ar"]

print(Fore.LIGHTWHITE_EX + "comandi:lista, per vedere le mosse disponibili del pezzo. exit, per uscire dal gioco")
dd = 0

for i in range(len(game_board)):
    dd += 1
    if i == 0:

        print(Fore.LIGHTWHITE_EX + ("_" * 32))
    else:
        print(Fore.LIGHTWHITE_EX + ("-" * 32))
    for j in range(len(game_board[i])):

        if game_board[i][j] in pezzi_rossi:
            if j == 7:
                print("|" + Fore.RED + game_board[i][j] + Fore.LIGHTWHITE_EX + "|" + " " + str(asse_y[dd]))
            else:
                print("|" + Fore.RED + game_board[i][j] + Fore.LIGHTWHITE_EX + "|", end="")
        elif game_board[i][j] in pezzi_bianchi:
            if j == 7:
                print("|" + Fore.CYAN + game_board[i][j] + Fore.LIGHTWHITE_EX + "|" + " " + str(asse_y[dd]))
            else:
                print("|" + Fore.CYAN + game_board[i][j] + Fore.LIGHTWHITE_EX + "|", end="")
        else:
            if j == 7:
                print("|" + Fore.LIGHTWHITE_EX + game_board[i][j] + "|" +  " " + str(asse_y[dd]))
            else:

                print("|" + Fore.LIGHTWHITE_EX + game_board[i][j] + "|", end="")


print("-" * 32)

for i in range(len(asse_x)):

     print(" " + asse_x[i] + " ", end=" ")

sss = 0
while Rerosso == True and Rebianco == True:

    posizione_pezzo = input("\n Scegli la posizione del pezzo da muovere (assey+assex): ")
    if posizione_pezzo == "exit":
        break

    y = assey_pos[int(posizione_pezzo[0])]
    x = assex_ps[posizione_pezzo[1]]


    lista_mosse = Move_set(game_board,posizione_pezzo)

    posizione_finale = input("Scegli la nuova posizione del pezzo:")
    while posizione_finale == "lista":
        print(lista_mosse)
        posizione_finale = input("Scegli la nuova posizione del pezzo:")
    if posizione_finale == "exit":
        break
    mossa = [int(posizione_finale[0]), posizione_finale[1]]
    mossa = mossa


    while mossa not in lista_mosse or lista_mosse == None:
        posizione_finale = input("Mossa non disponibile, scegline un'altra:")
        mossa = [int(posizione_finale[0]), posizione_finale[1]]
    y_f = assey_pos[int(posizione_finale[0])]
    x_f = assex_ps[posizione_finale[1]]
    if game_board[y_f][x_f] == "Rb":
        Rebianco = False

    elif game_board[y_f][x_f] == "Rr":
        print("ok")
        Rerosso = False

    game_board[y_f][x_f] = game_board[y][x]
    game_board[y][x] = "00"

    dd = 0
    for i in range(len(game_board)):
        dd += 1
        if i == 0:

            print(Fore.LIGHTWHITE_EX + ("_" * 32))
        else:
            print(Fore.LIGHTWHITE_EX + ("-" * 32))
        for j in range(len(game_board[i])):

            if game_board[i][j] in pezzi_rossi:
                if j == 7:
                    print("|" + Fore.RED + game_board[i][j] + Fore.LIGHTWHITE_EX + "|" + " " + str(asse_y[dd]))
                else:
                    print("|" + Fore.RED + game_board[i][j] + Fore.LIGHTWHITE_EX + "|", end="")
            elif game_board[i][j] in pezzi_bianchi:
                if j == 7:
                    print("|" + Fore.CYAN + game_board[i][j] + Fore.LIGHTWHITE_EX + "|" + " " + str(asse_y[dd]))
                else:
                    print("|" + Fore.CYAN + game_board[i][j] + Fore.LIGHTWHITE_EX + "|", end="")
            else:
                if j == 7:
                    print("|" + Fore.LIGHTWHITE_EX + game_board[i][j] + "|" + " " + str(asse_y[dd]))
                else:

                    print("|" + Fore.LIGHTWHITE_EX + game_board[i][j] + "|", end="")

    print("-" * 32)

    for i in range(len(asse_x)):
        print(" " + asse_x[i] + " ", end=" ")

if Rerosso == False:
    print("\nIl giocatore blu è il vincitore")
elif Rebianco == False:
    print("\nIl giocatore rosso è il vincitore")
