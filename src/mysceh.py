import cmd2
import os
import sys
import random
import datetime

class MySCEH(cmd2.Cmd):
    intro="DataGuard verified.\nMyCEC (complete).\n"
    prompt = "mycec(pyver)> "
    def msg_ok(self,txt):
        self.poutput(txt)
    def msg_err(self,txt):
        self.poutput(f"ERROR: {txt}")
    def do_printMsg(self,arg):
        self.msg_ok(arg)
    def do_createFile(self, args):
        "Create an empty file inside the current WorkDir."
        filename = args.strip()

        if not filename:
            self.poutput("Usage: CreateFile <filename>")
            return

    # Ruta final adentro de WorkDir
        full_path = os.path.join(self.wdir, filename)

        try:
        # Crear el archivo vacío
            with open(full_path, "w", encoding="utf-8") as f:
                pass

            self.msg_ok(f"Created: {filename}  (#in {self.wdir})")
        except Exception as e:
            self.msg_err(f"Error creating file: {e}")
    def do_del(self,arg):
        blocked = ('.dll','.fish','.exe','.ps1','.bat')
        if not arg.endswith(blocked):
            os.remove(arg)
        else:
            pass
    def default(self, line):
        cmd = line.split()[0]
        self.msg_err(f"Unknown command: {cmd}")
    def do_writeText(self, args):
        parts = args.split(" ", 1)
        if len(parts) < 2:
            self.poutput("Usage: WriteFile <filename> <text>")
            return

        filename, text = parts[0], parts[1]

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
            self.poutput(f"Written to {filename}")
        except Exception as e:
            self.msg_err(e)
    def do_createDir(self,arg):
        arg = arg.split("$", 1)[0].strip()
        if not arg:
            print("missing folder name.")
            return
        target = os.path.join(self.wdir, arg)
        try:
            if os.path.exists(target):
                print(f"Dir already exists: {arg}")
            else:
                os.makedirs(target)
                print(f"Dir created: {arg}")
        except Exception as e:
            self.msg_err(f"CreateDir Error: {e}")
    def do_listW(self,arg):
        print(os.listdir(self.wdir))
    def do_changeW(self, arg):
        path = arg.strip()
        if not path:
            print("You must specify a directory.")
            return

        '''# Convertir a ruta absoluta'''
        full = os.path.abspath(path)

        if os.path.isdir(full):
            self.wdir = full
            print(f"Working Dir changed to: #{self.wdir}")
        else:
            print("Invalid directory.")
    def do_changeV(self, arg):
        path = arg.strip()

        if not path:
            print("You must specify a directory.")
            return

        full = os.path.abspath(path)

        if os.path.isdir(full):
            self.vdir = full
            print(f"Vision Dir changed to: #{self.vdir}")
        else:
            print("Invalid directory.")
    def do_shPaths(self,arg):
        print(f"WorkDir: {self.wdir}\nVisualDir: {self.vdir}")
    def do_version(self,arg):
        arg = arg.lower()
        if arg == "mycec":
            print("MyCEC vPython (complete) v1.0.4")
        elif arg == "dataguard":
            f=open(f"DataGuard (DG) #{hex(104)}")
        elif arg == 'mainki':
            print(f"MainKi v1.1.0")
        elif arg== 'inp':
            print("MyInp (Mainki V) v1.1.0 Lists & Dicts.\nFastInp v0.0.0 (not released).")
        elif arg == 'fcontrol':
            print("FControl CPPV v0.0.3.\nFControl RSV v0.0.3.")
        elif arg in (r"\t", " "):
            print("Usage: Version {product}.")
        else:
            print(f"Unknown Item '{arg}'.")
    def do_exit(self,arg):
        print(f"Exiting...\n")
        return True
    def do_clearCmd(self,arg):
        os.system('cls' if os.name == 'nt' else 'clear')
        return
    def do_shInfo(self,arg):
        file = arg.strip()
        if not file:
            print("Usage: ShowInfo <file>")
            return
        path = os.path.join(self.wdir,file)
        if not os.path.exists(path):
            print("File not found.")
            return
        size = os.path.getsize(path)
        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
        try:
            create_time = datetime.datetime.fromtimestamp(os.path.getctime(path))
        except:
            create_time = "No disponible."
        lines = 0
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                for _ in f:
                    lines += 1
        except:
            lines = "No es archivo de texto."
        _, ext = os.path.splitext(path)
        print(f"""Info of file:
Name: {file}
Extension: {ext if ext else '(without extension)'}
Size: {size} bytes
Lines: {lines}
Created: {create_time}
Modificated: {mod_time}
Path: {path}""")
def do_pyExec(self,arg):
    if "pyDes" not in arg:
        self.msg_err("Missing 'pyDes'.")
        return
    code = arg.split("PyDes")[0].strip()
    if not code:
        self.msg_err("Expected code for execute.")
        return
    try:
        exec(code, {})
    except Exception as e:
        """
        # The line `self.poutput("[MyCEC] ERROR")` is calling the `poutput` method of the `cmd2.Cmd`
        # class instance (`self`) with the message "[MyCEC] ERROR" as an argument. This method is
        # typically used to output messages to the command line interface being used. In this case, it
        # would display the error message "[MyCEC] ERROR" to the user of the command line interface.
        """
        self.msg_err(f"Error executing Python: {e}")
if __name__ == "__main__":
    print("Select your working directory (leave empty to use current folder):")
    path = input().strip()

    if path == "":
        path = os.getcwd()


    if not os.path.isdir(path):
        print("Invalid directory. Using current folder instead.")
        path = os.getcwd()
    print(f"Working directory set to: {path}")
    app = MySCEH()
    app.wdir = path
    app.vdir = path
    app.cmdloop()