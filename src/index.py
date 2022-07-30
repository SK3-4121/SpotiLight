# Made by SK3
# Version 1.0.1
# Github: https://github.com/SK3-4121/SpotiLight

# THIS ONLY WORKS ON WINDOWS
# Note: for this to work on Mac, Linux you'll have to edit the code to get it to work.

import os, time, shutil, colorama

colorama.init(autoreset=True)
Fore = colorama.Fore
Green = Fore.GREEN
Blue = Fore.BLUE
Red = Fore.RED

SpotifyDirectory, loginFile, rootFile, zip_exec = None, None, None, None

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def hook_spotify():
    global loginFile, rootFile, SpotifyDirectory

    path = os.getenv('APPDATA')
    SpotifyDirectory = path + "\\Spotify\\"
    for filename in os.listdir(path+"/Spotify/Apps/"):
        if filename == "xpui.spa":
            rootFile = "xpui.spa"
        if filename == "login.spa":
            loginFile = "login.spa"

    if loginFile == None or rootFile == None:
        print(f"{Red}[-]: Failed to find file")
    else:
        print(f"{Green}[+]: Found File's [{loginFile, rootFile, SpotifyDirectory}]")
        loginFile = path + "\\Spotify\\Apps\\" + loginFile
        rootFile = path + "\\Spotify\\Apps\\" + rootFile

def hook_7zip():
    global zip_exec

    if os.path.exists("C:\Program Files\\7-Zip"):
        zip_exec = str("C:\Program Files\\7-Zip\\7z.exe")
        print(f"{Green}[+]: Found 7-Zip File [('{zip_exec}')]")
    else:
        print(f"{Red}[-]: Failed to find 7-Zip directory in Program Files")

def ask():
    print(f" [decompile]: Decompiles spotifys css/js source code\n [compile]: Compile your custom spotify source\n {Red}[rtsfe]: Real Time Spotify File Editing SOON{Fore.RESET}\n [rsc]: Reload Spotify Css kills and reopens are replaces the xpui and login spas (requires root)\n [rs]: Reload Spotify this kills and then reloads spotify from root\n [exit]: Exits")
    ask_input = str(input(f"{Blue}[*] What do you want us to run?{Fore.RESET}: "))
    ask_input = ask_input.lower()
    if ask_input == "decompile":
        return 1
    elif ask_input == "compile":
        return 2
    elif ask_input == "rtsfe":
        return 3
    elif ask_input == "rsc":
        return 4
    elif ask_input == "rs":
        return 5
    elif ask_input == "exit":
        return 6

def decompile():
    global zip_exec
    os.system("rm login/* || rm root/*")

    root_trm_cmd = str(f'"{zip_exec}" x {rootFile} -o./decompiled/root')
    os.system(root_trm_cmd)

    login_trm_cmd = str(f'"{zip_exec}" x {loginFile} -o./decompiled/login')
    os.system(login_trm_cmd)

def compile():
    global zip_exec
    os.chdir("compiled")
    os.system('"clear.bat"')

    root_trm_cmd = str(f'"{zip_exec}" a -tzip xpui.spa ../decompiled/root/*')
    os.system(root_trm_cmd)

    login_trm_cmd = str(f'"{zip_exec}" a -tzip login.spa ../decompiled/login/*')
    os.system(login_trm_cmd)

def __main__():
    global SpotifyDirectory
    clear()
    def Lines(character,count):
        whole = ""
        for i in range(count):
            whole = f"{whole}{character}"
        return str(whole)

    def rainbow():
        # SpotiLight
        return f'{Red}S{Fore.YELLOW}P{Green}O{Blue}T-{Blue}L{Green}I{Fore.YELLOW}G{Blue}H{Fore.MAGENTA}T{Fore.RESET}'

    size = os.get_terminal_size()
    columns = size.columns
    print(f"\n\n{Lines(' ',int(columns/2-10))}{rainbow()}\n\n{Lines('~',columns)}")
    hook_spotify()
    hook_7zip()
    print(f'{Blue}[!]: https://github.com/SK3-4121/SpotiLight')
    ask_command = ask()
    if ask_command == 1:
        decompile()
        print(f'{Green}[+]: decompiled spotify into the "/decompiled"!{Fore.RESET}')
    elif ask_command == 2:
        compile()
        print(f'{Green}[+]: Compiled spotify spa to the "/compiled"!{Fore.RESET}')
    elif ask_command == "3":
        print(f'{Red}[-]: Failed to launch an unstable command.')
    elif ask_command == 4:
        shutil.copy2("compiled/xpui.spa", str(f"{SpotifyDirectory}\\Apps\\xpui.spa"))
        shutil.copy2("compiled/login.spa", str(f"{SpotifyDirectory}\\Apps\\login.spa"))
        print(f"{Green}[+]: Updated the Spotify SPA's aka css files")
        os.system(f"taskkill /im Spotify.exe /F")
        print(f'{Green}[+]: Killed spotify (theres no check if it was open btw) it just kills it lol')
        time.sleep(1/9)
        os.startfile(f'{SpotifyDirectory}Spotify.exe')
        print(f'{Green}[+]: Reloaded Spotify')
    elif ask_command == 5:
        os.system(f"taskkill /im Spotify.exe /F")
        print(f'{Green}[+]: Killed spotify (theres no check if it was open btw) it just kills it lol')
        time.sleep(1/9)
        os.startfile(f'{SpotifyDirectory}Spotify.exe')
        print(f'{Green}[+]: Reloaded Spotify')
    elif ask_command == 6:
        print("Closing . . .")
        os.system("exit();")

if __name__ == "__main__":
    __main__()
