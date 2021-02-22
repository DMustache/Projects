from math import pi, cos, sin
import curses, locale, random, subprocess

POS_X, POS_Y, POS_A = 2, 2, 0
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
    for i in range(20):
        random.seed(i)
        noise = [random.randint(1, 2) for i in range(mapsize)]
        numList.append(adjacent_min(noise))

    for i in range(len(numList)):
        for j in range(len(numList[0])):
            if j == 0:
                MAP += '\n'

            if numList[i][j] == 1:
                MAP += '.'
            else:
                MAP += '#'

    return MAP

MAP = ''
MAP = createMap(MAP)

f = open(r'txt.txt', mode='w')
f.write(MAP)
f.close()

subprocess.Popen(['notepad.exe', r'txt.txt'])

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

    pos_x, pos_y, pos_a = POS_X, POS_Y, POS_A

    exit_flag = False
    while not exit_flag:
        screen_height, screen_width = screen.getmaxyx()

        for col in range(screen_width):
            ray_angle = (pos_a - user_angle / 2) + (col / screen_width) * user_angle

            eye_x, eye_y = sin(ray_angle), cos(ray_angle)

            leng = 0.0
            while leng < unHiden_zone:
                leng += resol
                test_y = int(pos_y + eye_y * leng)
                test_x = int(pos_x + eye_x * leng)
                if get_block(test_x, test_y) == '#':
                    break

            ceiling = int(screen_height / 2 - screen_height / leng)
            floor = int(screen_height - ceiling)

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

        screen.addstr(screen_height - 1, 0, f"x = {pos_x:.2f}, y = {pos_y:.2f}, a = {pos_a:.2f}")

        screen.refresh()

        key_code = screen.getch()
        key = chr(key_code) if 0 < key_code < 256 else 0
        if key in ('w', 's'):
            dx, dy = sin(pos_a) * spd, cos(pos_a) * spd
            if key == 's':
                dx, dy = -dx, -dy
            pos_x += dx
            pos_y += dy
            if get_block(POS_X, pos_y) == '#':
                pos_x -= dx
                pos_y -= dy
        elif key == 'a':
            pos_a -= rot_spd
        elif key == 'd':
            pos_a += rot_spd
        elif key == chr(27):
            break

    curses.endwin()


curses.wrapper(consWalker)