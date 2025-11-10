from Colors import Colors

class Logger:
    def __init__(self, debug=False):
        self.default_color = Colors.DEFAULT
        self.buffer = ""
        self.debug_mode = debug
        pass

    def print(self, msg, color=Colors.DEFAULT):
        """ Print into stdout """
        print(color.value + msg + self.default_color.value)

    def print_rainbow(self, msg):
        """ Print with rainbow colors """
        color_loop = [
            Colors.PURPLE,
            Colors.BLUE,
            Colors.GREEN,
            Colors.YELLOW,
            Colors.ORANGE,
            Colors.DARK_ORANGE,
            Colors.RED,
            Colors.PINK
        ]
        for index in range(len(msg)):
            color = color_loop[index % len(color_loop)]
            print(color.value + msg[index], end='')
            
        print(self.default_color.value)

    def log(self, msg, print=True):
        """ Register a log, and print it (default) """
        str = "[LOG]\t - " + msg
        self.buffer += str + "\n"
        
        if print:
            self.print(str)

    def warn(self, msg, print=True):
        """ Register a warning log [PURPLE] """
        str = "[WARN]\t - " + msg
        self.buffer += str + "\n"
        
        if print:
            self.print(str, color=Colors.PURPLE)
    
    def error(self, msg, print=True):
        """ Register an error log [RED] """
        str = "[ERROR]\t - " + msg
        self.buffer += str + "\n"
        
        if print:
            self.print(str, color=Colors.RED)
    
    def success(self, msg, print=True):
        """ Register a success log [GREEN] """
        str = "[SUCCES] - " + msg
        self.buffer += str + "\n"
        
        if print:
            self.print(str, color=Colors.GREEN)
    
    def fail(self, msg, print=True):
        """ Register a fail log [RED] """
        str = "[FAILED] - " + msg
        self.buffer += str + "\n"
        
        if print:
            self.print(str, color=Colors.RED)

    def debug(self, msg):
        """ Print a debug output. Can be disabled setting self.debug = False """
        str = "[DEBUG]\t - " + msg
        self.buffer += str + "\n"
        
        if self.debug_mode:
            self.print(str, color=Colors.YELLOW)

    def section(self, name, length=80, char=".", padding=2, color=Colors.DEFAULT):
        """ Create a separator to differenciate sections in log """
        remaining = length - len(name)
        half = remaining // 2
        print(
            color.value
            + "\n" * padding
            + char * (half - 1)
            + f" {name} "
            + char * (remaining - half - 1)
            + "\n" * (padding - 1)
            + self.default_color.value
        )
    
    def cadre(self, name, length=80, padding=1, color=Colors.DEFAULT):
        """ Print a rectangle avec le nom au milieu """
        remaining = length - len(name)
        half = remaining // 2
        char = "#"
        print(color.value)
        print(char * length)
        print((char + " " * (length - 2) + char + "\n") * padding, end="")
        print(
            "#" + " " * (half - 2)
            + f" {name} "
            + " " * (remaining - half - 2) + "#" + "\n",
            end=""
        )
        print((char + " " * (length - 2) + char + "\n") * padding, end="")
        print(char * length)
        print(self.default_color.value)
    
    def save(self, path="./file.log"):
        """ Save logs into logfile """
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.buffer)
            self.success(f"Logs saved to {path}")
        except Exception as e:
            self.fail(f"Could not save logs: {e}")

