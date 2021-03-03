import curses


def scr(stdscr):
    while True:
        key = stdscr.getch()
        stdscr.addstr(0,0," "*4)
        stdscr.addstr(0,0,str(key))

curses.wrapper(scr)
        
    
