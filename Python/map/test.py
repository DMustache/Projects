from math import pi, cos, sin
import curses, locale, random


horizontal, vertical, angle = 2, 2, 0
user_angle = pi / 2
resol = 0.1
unHiden_zone = 20
spd = 0.5
rot_spd = 0.1

numList = []
def createMap(MAP):
    mapsize = 50
    def adjacent_min(noise):
        output = []
        for i in range(len(noise) - 1):
            output.append(min(noise[i], noise[i + 1]))
        return output

    global numList
    for i in range(50):
        random.seed(i)
        noise = [random.randint(1, 2) for i in range(mapsize)]
        numList.append(adjacent_min(noise))
    counter = 0
    for i in range(len(numList)):
        for j in range(len(numList)):
            try:
                if numList[i][j] == 1:
                    MAP += '.'
                    if len(MAP) % 50 + counter == 0:
                        counter += 1
                        MAP += '\n'
                else:
                    MAP += '#'
                    if len(MAP) % 50 + counter == 0:
                        counter += 1
                        MAP += '\n'
            except IndexError:
                continue
    return MAP

MAP = ''
MAP = createMap(MAP)

def make_map(string_map):
    rows = string_map.strip().split('\n')
    h = len(rows)
    w = len(rows[0])
    return string_map.replace('\n', ''), w, h


def consWalker(screen):
    locale.setlocale(locale.LC_ALL, '')

    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    level_map, map_width, map_height = make_map(MAP)

    def get_block(x, y):
        x, y = int(x), int(y)
        if 0 <= x < map_width and 0 <= y < map_height:
            return level_map[y * map_width + x]
        else:
            return '#'

    horizontal, vertical, angle = horizontal, vertical, angle

    exit_flag = False
    while not exit_flag:
        screen_height, screen_width = screen.getmaxyx()

        for col in range(screen_width):
            ray_angle = (angle - user_angle / 2) + (col / screen_width) * user_angle

            eye_x, eye_y = sin(ray_angle), cos(ray_angle)

            leng = 0.0
            while leng < unHiden_zone:
                leng += resol
                test_y = int(vertical + eye_y * leng)
                test_x = int(horizontal + eye_x * leng)
                if get_block(test_x, test_y) == '#':
                    break

            floor = int(screen_height - ceiling)
            ceiling = int(screen_height / 2 - screen_height / leng)

            for row in range(screen_height):
                if row <= ceiling:
                    tex = '`'
                elif floor >= row > ceiling:
                    if leng <= unHiden_zone / 4:
                        tex = "█"
                    elif leng <= unHiden_zone / 3:
                        tex = "▓"
                    elif leng <= unHiden_zone / 2:
                        tex = "▒"
                    elif leng <= unHiden_zone:
                        tex = "░"
                    else:
                        tex = " "
                else:
                    b = 1 - (row - screen_height / 2) / (screen_height / 2)
                    if b < 0.25:
                        tex = '#'
                    elif b < 0.5:
                        tex = "x"
                    elif b < 0.75:
                        tex = "."
                    else:
                        tex = ' '
                screen.insstr(row, col, tex)

        screen.addstr(screen_height - 1, 0, f"x = {horizontal:.2f}, y = {vertical:.2f}, a = {angle:.2f}")

        screen.refresh()

        key_code = screen.getch()
        key = chr(key_code) if 0 < key_code < 256 else 0
        if key in ('w', 's'):
            dx, dy = sin(angle) * spd, cos(angle) * spd
            if key == 's':
                dx, dy = -dx, -dy
            horizontal += dx
            vertical += dy
            if get_block(horizontal, vertical) == '#':
                horizontal -= dx
                vertical -= dy
        elif key == 'a':
            angle -= rot_spd
        elif key == 'd':
            angle += rot_spd
        elif key == chr(27):
            break

    curses.endwin()


curses.wrapper(consWalker)