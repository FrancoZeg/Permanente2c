import curses
import random
import time

nombre = input("¿CUÁL ES SU NOMBRE USUARIO?\n")
nombre_upper = nombre.upper()
print ("MUY BIEN, " + nombre_upper + " EMPECEMOS")
time.sleep(1)


suerte1 = [1,1,1,2,1,1,1,2,2,2]
suerte2 = [1,1,1,2,1,1,1,2,1,1]
suerte3 = [1,1,1,2,1,2,1,2,1,1] 

class enemigo:
    def __init__(self, nombreP, vidaP, ataqueP):
        self.nombreP = nombreP
        self.vidaP = vidaP
        self.ataqueP = ataqueP

class jugador:
    def __init__(self, nombreJ, vidaJ, ataqueJ, equipamento):
        self.nombreJ = nombreJ
        self.vidaJ = vidaJ
        self.ataqueJ = ataqueJ
        self.equipamento = equipamento

def print_menu(stdscr, vidaJ, nombreJ, ataqueJ, vidaP, nombreP, ataqueP):
    stdscr.clear()
    stdscr.addstr(0, 25 , "---------------EL {} SE INTERPUSO EN TU CAMINO---------------".format(nombreP))
    stdscr.addstr(1, 43, "{} ------- {} PV Y {} DE DAÑO".format(nombreJ, vidaJ, ataqueJ))
    stdscr.addstr(10, 70, "{} ------- {} PV Y {} DE DAÑO".format(nombreP, vidaP, ataqueP))
    stdscr.addstr(11, 80, "─────▄█▄█─────────────")
    stdscr.addstr(12, 80, "────█████▄▄▄──────────")
    stdscr.addstr(13, 80,"──────███████▄────────")
    stdscr.addstr(14, 80,"______█▀█▀█████_______")
    stdscr.addstr(15, 80,"_____▄█▄█__▄█▄█_______")
    stdscr.addstr(10, 25, "       \          ")
    stdscr.addstr(11, 25, "        \O        ")
    stdscr.addstr(12, 25, "         |\/      ")
    stdscr.addstr(13, 25, "         |        ")
    stdscr.addstr(14, 25, "        / \       ")
    stdscr.addstr(15, 25, "      _/   \_     ")
    stdscr.addstr(2, 0, "---------------MENÚ---------------")
    stdscr.addstr(3, 0, "PRESIONA → PARA ATACAR")
    stdscr.addstr(6, 0, "PRESIONA ↓ PARA REVISAR LOS ATAQUES COMPUESTOS")
    stdscr.addstr(4, 0, "PRESIONA ↑ PARA VER LA MOCHILA")
    stdscr.addstr(5, 0, "PRESIONA ← PARA ESCAPAR")
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def escapar(esc_confirm):
    esc = random.choice(suerte2)
    if esc == 1:
        esc_confirm = True
        return esc_confirm
    if esc == 2:
        esc_confirm = False
        return esc_confirm

def mochila(stdscr):
    stdscr.clear()
    text1 = "MENÚ DE MOCHILA"
    text2 = "PRESIONA → PARA EQUIPARTE EL BATE"
    text3 = "PRESIONA ← PARA TOMAR AGUA"
    text4 = "PRESIONA CUALQUIER OTRA TECLA PARA VOLVER"
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    x3 = w//2 - len(text3)//2
    x4 = w//2 - len(text4)//2
    y = h//2
    stdscr.addstr(y - 1, x, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.addstr(y + 1, x3, text3)
    stdscr.addstr(y+2, x4, text4)
    stdscr.refresh()

def bate(stdscr, objetoB):
    stdscr.clear()
    text1 = "AHORA TIENES EQUIPADO EL BATE"
    text2 = "YA TIENES EQUIPADO EL BATE, ¿QUÉ ESPERAS PARA ATACAR?"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    if objetoB == True:
        stdscr.addstr(y, x2, text2)
    else:
        stdscr.addstr(y, x1, text1)
    stdscr.refresh()

def botella(stdscr):
    stdscr.clear()
    text = "TOMASTE UN POCO DE AGUA"
    botella1 = "       [-]    "
    botella2 = "     .-'-'-.  "
    botella3 = "    |;::    | "
    botella4 = "    |;::-.._| "
    botella5 = "    '-.._..-' "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    xbotella = w//2 - len(botella1)//2
    stdscr.addstr(y, x, text)
    stdscr.addstr(y + 1, xbotella, botella1)
    stdscr.addstr(y + 2, xbotella, botella2)
    stdscr.addstr(y + 3, xbotella, botella3)
    stdscr.addstr(y + 4, xbotella, botella3)
    stdscr.addstr(y + 5, xbotella, botella4)
    stdscr.addstr(y +6 , xbotella, botella5)
    stdscr.refresh()

def botella10075(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO LLENA"
    text2 = "VAYA DESPERDICIO..."
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella10050(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ LLENA HASTA LA MITAD"
    text2 = "VAYA DESPERDICIO..."
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella10025(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO VACÍA"
    text2 = "VAYA DESPERDICIO..."
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella7575(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO LLENA"
    text2 = "BIEN"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella7550(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ LLENA HASTA LA MITAD"
    text2 = "BIEN"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella7525(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO VACÍA"
    text2 = "BIEN"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella075(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO LLENA"
    text2 = "¡¡¡REFRESCANTE!!!"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella050(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ LLENA HASTA LA MITAD"
    text2 = "¡¡¡REFRESCANTE!!!"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella025(stdscr):
    stdscr.clear()
    text1 = "LA BOTELLA ESTÁ MEDIO VACÍA"
    text2 = "¡¡¡REFRESCANTE!!!"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y + 1, x1, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.refresh()

def botella_vacia(stdscr):
    stdscr.clear()
    text1 = "PUEDES VER CON TRISTEZA UNA BOTELLA VACÍA :c"
    h, w =stdscr.getmaxyx()
    x1 = w//2 - len(text1)//2
    y = h//2
    stdscr.addstr(y, x1, text1)
    stdscr.refresh()

def ataques(stdscr):
    stdscr.clear()
    text1 = "MENÚ DE MOCHILA"
    text2 = "PRESIONA → PARA EJECUTAR MOVIMIENTOS DE JUDO"
    text3 = "PRESIONA ← PARA TIRAR UNA PIEDRA INVISIBLE"
    text4 = "PRESIONA CUALQUIER OTRA TECLA PARA VOLVER"
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text1)//2
    x2 = w//2 - len(text2)//2
    x3 = w//2 - len(text3)//2
    x4 = w//2 - len(text4)//2
    y = h//2
    stdscr.addstr(y - 1, x, text1)
    stdscr.addstr(y, x2, text2)
    stdscr.addstr(y + 1, x3, text3)
    stdscr.addstr(y+2, x4, text4)
    stdscr.refresh()

def judo(stdscr):
    stdscr.clear()
    texta = "¡¡¡TOMA!!!"
    text = "    _______       "
    text1 = "---'   ____)____  "
    text2 = "          ______) "
    text3 = "          _______)"
    text4 = "         _______) "
    text5 = "---.__________)   "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    xa = w//2 - len(texta)//2
    y = h//2
    stdscr.addstr(y - 3, xa, texta)
    stdscr.addstr(y - 2, x, text)
    stdscr.addstr(y - 1, x, text1)
    stdscr.addstr(y, x, text2)
    stdscr.addstr(y + 1, x, text3)
    stdscr.addstr(y + 2, x, text4)
    stdscr.addstr(y + 3, x, text5)
    stdscr.refresh()

def movimientos_de_judo(vidaC):
    precision = random.choice(suerte1)
    if precision == 1:
        vidaC = vidaC
        return vidaC
    else:
        vidaC -= 25
        return vidaC

def piedra_invisible(esc_confirm):
    precision1 = random.choice(suerte3)
    if precision1 == 1:
        return esc_confirm
    else:
        esc_confirm = False
        return esc_confirm

def malasuerte(stdscr):
    stdscr.clear()
    texta = "FALLASTE..."
    text = "    _._  "
    text1 = "   / O \ "
    text2 = "   \| |/ "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    xa = w//2 - len(texta)//2
    y = h//2
    stdscr.addstr(y - 3, xa, texta)
    stdscr.addstr(y - 2, x, text)
    stdscr.addstr(y - 1, x, text1)
    stdscr.addstr(y, x, text2)
    stdscr.refresh()

def escape_fallido(stdscr):
    stdscr.clear()
    text = "EL PERRO IMPIDIÓ TU HUIDA"
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def escape_exitoso(stdscr):
    stdscr.clear()
    text = "¡¡¡LOGRASTE ESCAPAR!!!"
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.addstr(y + 2, x + 5 , "     o__")
    stdscr.addstr(y + 3, x + 5, "  \_/   ")
    stdscr.addstr(y + 4, x + 5, "    |   ")
    stdscr.refresh()

def ganador(stdscr):
    stdscr.clear()
    texta = "  ________    _____    _______      _____    _______________________________ "
    text1 = " /  _____/   /  _  \   \      \    /  _  \  /   _____/\__    ___/\_   _____/ "
    text2 = "/   \  ___  /  /_\  \  /   |   \  /  /_\  \ \_____  \   |    |    |    __)_  "
    text3 = "\    \_\  \/    |    \/    |    \/    |    \/        \  |    |    |        \ "
    text4 = " \______  /\____|__  /\____|__  /\____|__  /_______  /  |____|   /_______  / "
    text5 = "        \/         \/         \/         \/        \/                    \/  "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text1)//2
    xa = w//2 - len(texta)//2
    y = h//2
    stdscr.addstr(y - 3, xa, texta)
    stdscr.addstr(y - 2, x, text1)
    stdscr.addstr(y - 1, x, text2)
    stdscr.addstr(y, x, text3)
    stdscr.addstr(y + 1, x, text4)
    stdscr.addstr(y + 2, x, text5)
    stdscr.refresh()

def perdedor(stdscr):
    stdscr.clear()
    texta = "PIERDES..."
    text1 = "  _____  "
    text2 = " /     \ "
    text3 = "| () () |"
    text4 = " \  ^  / "
    text5 = "  |||||  "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text1)//2
    xa = w//2 - len(texta)//2
    y = h//2
    stdscr.addstr(y - 3, xa, texta)
    stdscr.addstr(y - 2, x, text1)
    stdscr.addstr(y - 1, x, text2)
    stdscr.addstr(y, x, text3)
    stdscr.addstr(y + 1, x, text4)
    stdscr.addstr(y + 2, x, text5)
    stdscr.refresh()

def escapeE(stdscr):
    stdscr.clear()
    texta = "EL PERRO ESCAPÓ AULLANDO"
    text1 = "                .--~~,__  "
    text2 = "   :-....,-------`~~'._.' "
    text3 = "    `-,,,  ,_      ;'~U'  "
    text4 = "     _,-' ,'`-__; '--.    "
    text5 = "    (_/'~~      ''''(;        "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text1)//2
    xa = w//2 - len(texta)//2
    y = h//2
    stdscr.addstr(y - 3, xa, texta)
    stdscr.addstr(y - 2, x, text1)
    stdscr.addstr(y - 1, x, text2)
    stdscr.addstr(y, x, text3)
    stdscr.addstr(y + 1, x, text4)
    stdscr.addstr(y + 2, x, text5)
    stdscr.refresh()

def ataque_jugador(stdscr, equipamento):
    text = "888                                   "
    text2 = "88888b.  .d88b.  .d88b. 88888b.d88b.  "
    text3 = "888  88bd88  88bd88  88b888  888  88b "
    text4 = "888  888888  888888  888888  888  888 "
    text5 = "888 d88PY88..88PY88..88P888  888  888 "
    text6 = "88888P    Y88P    Y88P  888  888  888 "
    texta1 = "HICISTE 12 DE DAÑO"
    texta2 = "HICISTE 18 DE DAÑO"
    stdscr.clear()
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    xa = w//2 - len(texta1)//2
    stdscr.addstr(y - 5, x, text)
    stdscr.addstr(y - 4, x, text)
    stdscr.addstr(y - 3, x, text)
    stdscr.addstr(y - 2, x, text2)
    stdscr.addstr(y - 1, x, text3)
    stdscr.addstr(y, x, text4)
    stdscr.addstr(y + 1, x, text5)
    stdscr.addstr(y + 2, x, text6)
    if equipamento == True:
        stdscr.addstr(y + 4, xa, texta2)
    else:
        stdscr.addstr(y + 4, xa, texta1)
    stdscr.refresh()

def ataque_enemigo(stdscr, text):
    stdscr.clear()
    text2 = "            |\   "
    h, w =stdscr.getmaxyx()
    x = w//2 - len(text)//2
    x2 = w//2 - len(text2)//2
    y = h//2
    stdscr.addstr(y - 3, x, text)
    stdscr.addstr(y - 2, x2, "            |\   ")
    stdscr.addstr(y - 1, x2, "   \`-. _.._| \  ")
    stdscr.addstr(y, x2, "    |_,'  __`. \ ")
    stdscr.addstr(y + 1, x2, "    (.\ _/.| _  |")
    stdscr.addstr(y + 2, x2, "   ,'      __ \ |")
    stdscr.addstr(y + 3, x2, " ,'     __/||\  |")
    stdscr.addstr(y + 4, x2, "(--)  ,/|||||/  |")
    stdscr.addstr(y + 5, x2, "   `-'_----    / ")
    stdscr.addstr(y + 6, x2, "      /`-._.-'/  ")
    stdscr.addstr(y + 7, x2, "      `-.__.-'   ")

    stdscr.refresh()

def main(stdscr):
    esc_conf = True
    DatosEnemigo = enemigo("PERRO ENORME", 95, 10)
    DatosJugador = jugador(str(nombre_upper), 100, 12, False)
    curses.curs_set(False)
    botella_de_agua = 100
    while DatosEnemigo.vidaP > 0 and DatosJugador.vidaJ > 0 and esc_conf == True:
        x = DatosJugador.vidaJ
        y = DatosJugador.equipamento
        print_menu(stdscr, DatosJugador.vidaJ, DatosJugador.nombreJ, DatosJugador.ataqueJ, DatosEnemigo.vidaP, DatosEnemigo.nombreP, DatosEnemigo.ataqueP)
        key = stdscr.getch()
        while key == curses.KEY_UP:
            mochila(stdscr)
            eleccionm = stdscr.getch()
            if eleccionm == curses.KEY_RIGHT:
                bate(stdscr, y)
                time.sleep(2)
                DatosJugador = jugador(str(nombre_upper), x, 18, True)
                time.sleep(0.5)
                ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                time.sleep(3)
                DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                break
            elif eleccionm == curses.KEY_LEFT:
                while botella_de_agua > 0:
                    botella(stdscr)
                    botella_de_agua -= 25
                    time.sleep(2)
                    if x == 100 and botella_de_agua > 0:
                        vida_com = 100 - x
                        x += vida_com
                        DatosJugador = jugador(str(nombre_upper), x, 12, False)
                        if botella_de_agua == 75:
                            botella10075(stdscr)
                            time.sleep(2)
                        elif botella_de_agua == 50:
                            botella10050(stdscr)
                            time.sleep(2)
                        else:
                            botella10025(stdscr)
                            time.sleep(2)
                    elif x <= 75 and botella_de_agua > 0:
                        vida_com = 100 - x
                        x += vida_com
                        DatosJugador = jugador(str(nombre_upper), x, 12, False)
                        if botella_de_agua == 75:
                            botella075(stdscr)
                            time.sleep(2)
                        elif botella_de_agua == 50:
                            botella050(stdscr)
                            time.sleep(2)
                        else:
                            botella025(stdscr)
                            time.sleep(2)
                    elif x > 75 and x < 100 and botella_de_agua > 0:
                        vida_com = 100 - x
                        x += vida_com
                        DatosJugador = jugador(str(nombre_upper), x, 12, False)
                        if botella_de_agua == 75:
                            botella7575(stdscr)
                            time.sleep(2)
                        elif botella_de_agua == 50:
                            botella7550(stdscr)
                            time.sleep(2)
                        else:
                            botella7525(stdscr)
                            time.sleep(2)
                    time.sleep(0.5)
                    ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                    time.sleep(3)
                    DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                    break
                else:
                    botella_vacia(stdscr)
                    time.sleep(2)
                break
            else:
                menu = False
                break
        while key == curses.KEY_DOWN:
            ataques(stdscr)
            eleccionAtaques = stdscr.getch()
            if eleccionAtaques == curses.KEY_RIGHT:
                xa = x
                x = movimientos_de_judo(x)
                if xa != x:
                    DatosEnemigo.vidaP -= 25
                    judo(stdscr)
                    time.sleep(2)
                    time.sleep(0.5)
                    ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                    time.sleep(3)
                    DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                    break
                else:
                    malasuerte(stdscr)
                    time.sleep(2)
                    time.sleep(0.5)
                    ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                    time.sleep(3)
                    DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                    break
            elif eleccionAtaques == curses.KEY_LEFT:
                e = esc_conf
                esc_conf = piedra_invisible(esc_conf)
                if e!= esc_conf:
                    escapeE(stdscr)
                    esc_conf = False
                    time.sleep(2)
                    break
                else:
                    malasuerte(stdscr)
                    time.sleep(2)
                    time.sleep(0.5)
                    ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                    time.sleep(3)
                    DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                    break
            else:
                menu = False
                break
        while key == curses.KEY_LEFT:
            esc_conf = escapar(esc_conf)
            if esc_conf  == True:
                escape_fallido(stdscr)
                time.sleep(2)
                time.sleep(0.5)
                ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                time.sleep(3)
                DatosJugador.vidaJ -= DatosEnemigo.ataqueP
                break
            else:
                escape_exitoso(stdscr)
                time.sleep(2)
                break
        while key == curses.KEY_RIGHT:
            if y == False:
                DatosEnemigo.vidaP -= DatosJugador.ataqueJ
                ataque_jugador(stdscr, y)
                time.sleep(2)
                time.sleep(0.5)
                ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                time.sleep(3)
                DatosJugador.vidaJ -= DatosEnemigo.ataqueP
            else:
                DatosEnemigo.vidaP -= DatosJugador.ataqueJ
                ataque_jugador(stdscr, y)
                time.sleep(2)
                time.sleep(0.5)
                ataque_enemigo(stdscr, "EL PERRO ENORME HIZO 10 DE DAÑO")
                time.sleep(3)
                DatosJugador.vidaJ -= DatosEnemigo.ataqueP
            break
    else:
        if DatosEnemigo.vidaP <= 0:
            ganador(stdscr)
            time.sleep(2)
        elif DatosJugador.vidaJ <= 0:
            perdedor(stdscr)
            time.sleep(2)
            

curses.wrapper(main)