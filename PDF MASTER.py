import PyPDF2
import pikepdf
import time
import pyttsx3
import os
while True:
    try:
        def outer_func(colour):
            def inner_function(msg):
                print(f'{colour}{msg}')
            return inner_function
        ''' COLOUR PRINTS '''
        BLUE = outer_func("\u001b[34m")
        GREEN = outer_func('\033[92m')
        YELLOW = outer_func('\033[93m')
        RED = outer_func('\033[91m')
        MAGENTE = outer_func("\u001b[35m")
        CYAN = outer_func("\u001b[36m")
        def banner():
            CYAN(r'''
            
                            __________________  ___________        _____      _____    _________________________________________ 
                            \______   \______ \ \_   _____/       /     \    /  _  \  /   _____/\__    ___/\_   _____/\______   \
                            |     ___/|    |  \ |    __)        /  \ /  \  /  /_\  \ \_____  \   |    |    |    __)_  |       _/
                            |    |    |    `   \|     \        /    Y    \/    |    \/        \  |    |    |        \ |    |   \
                            |____|   /_______  /\___  /        \____|__  /\____|__  /_______  /  |____|   /_______  / |____|_  /
                                            \/     \/                 \/         \/        \/                    \/         \/ 
    Created by Selemon Brahanu
    PDF MASTER V1.0''')
        banner()
        print("\033[92mpppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp\n")
        choose = input("\033[92m1:PDF Encrypter\n"
                    "2:PDF Bruteforcer\n"
                    "3:Audiobook\n"
                    "4:PDF Decrypter\n"
                    "5.PDF Reader\n"
                    "6.Exit\n\n"
                    "[+] Enter your desired choice: ")
        time.sleep(2)
        if choose == "1":
            os.system('clear')
            def banner():
                YELLOW(r'''
            __________________  ___________ ___________ _______  ________________________.___.__________________________________________ 
            \______   \______ \ \_   _____/ \_   _____/ \      \ \_   ___ \______   \__  |   |\______   \__    ___/\_   _____/\______   \
            |     ___/|    |  \ |    __)    |    __)_  /   |   \/    \  \/|       _//   |   | |     ___/ |    |    |    __)_  |       _/
            |    |    |    `   \|     \     |        \/    |    \     \___|    |   \\____   | |    |     |    |    |        \ |    |   \
            |____|   /_______  /\___  /    /_______  /\____|__  /\______  /____|_  // ______| |____|     |____|   /_______  / |____|_  /
                            \/     \/             \/         \/        \/       \/ \/                                    \/         \/ 
        
                                                        ⠀⠀⠀⠀⠀⠀⣀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣄⣀⡀
                                                        ⠀⠀⠀⢀⣠⣾⣿⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣦⡀
                                                        ⠀⠀⠀⣸⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣇
                                                        ⠀⠀⣾⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣷
                                                        ⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
                                                        ⣶⣶⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣶⣶⡆
                                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
                                                        ⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁                 
        
            Created by Selemon Brahanu
            PDF ENCRYPTER V1.0  
            ''')
            banner()
            print('\033[92mxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            try:
                book = input(u'\033[93m[+]Enter the pdf you want to encrypt: ')
                pdfreader = PyPDF2.PdfFileReader(book)
                pdfwriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfreader.numPages):
                    pdfwriter.addPage(pdfreader.getPage(pageNum))
                password = input('\033[93m'"[+]Enter password you want to encrypt with: ")
                pdfwriter.encrypt(password)
                name = input('\033[93m'"[+]Enter the new name for your encrypted pdf: ")
                resultpdf = open(name, "wb")
                pdfwriter.write(resultpdf)
                resultpdf.close()
                print(u'\033[91m'"[+]PDF HAS BEEN ENCRYPTED")
            except:
                print('\033[91m'"The pdf is  ENCRYPTED...................Please enter another file.........................")
        if choose == "2":
            os.system('clear')
            def banner():
                RED('''
            __________________________   _____________________  __________________________________________________________________ 
            ___  __ \__  __ \__  ____/   ___  __ )__  __ \_  / / /__  __/__  ____/__  ____/_  __ \__  __ \_  ____/__  ____/__  __ \
            __  /_/ /_  / / /_  /_       __  __  |_  /_/ /  / / /__  /  __  __/  __  /_   _  / / /_  /_/ /  /    __  __/  __  /_/ /
            _  ____/_  /_/ /_  __/       _  /_/ /_  _, _// /_/ / _  /   _  /___  _  __/   / /_/ /_  _, _// /___  _  /___  _  _, _/ 
            /_/     /_____/ /_/          /_____/ /_/ |_| \____/  /_/    /_____/  /_/      \____/ /_/ |_| \____/  /_____/  /_/ |_|
        
                                                    ⠀⠀⠀⣴⣾⣿⣿⡿⠇
                                                    ⠀⠀⠀⣶⣿⣿⣿⠉⠀⠀⠀⠀⢰⣶⣶⣶⣦⣀
                                                    ⠀⠀⠀⣿⣿⣯⣄⠀⠀⠀⠀⠀⠘⠛⠛⠛⠿⣿⣷⣦⣄
                                                    ⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
                                                    ⠀⠀⠀⠀⣴⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
                                                    ⣀⣴⣶⣶⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣷⣦⣀
                                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                    ⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛
                                                    ⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁
        
            Created by Selemon Brahanu
            PDF BRUTEFORCER V1.0                                                                                                                                                                                                                                                                                
            ''')


            banner()
            print(
                '\033[91m'".....................................................PDF BRUTEFORCER LOADING........................................")
            print(
                '\033[91m'".....................................................PDF BRUTEFORCER RUNNING........................................\n")
            wordlist = input("\033[91m[+] Enter the wordlist you want to use: ")
            pdf = input("\033[91m[+] Enter pdf you want to bruteforce: ")
            file = open(wordlist)
            for password in file:
                try:
                    with pikepdf.open(pdf, password.strip()) as pdf:
                        print('\033[92m'"Password found: {}".format(password))
                        break
                except:
                    print('\033[91m'"Trying password: {}".format(password), '\033[92m')
                    continue

        if choose == "4":
            os.system('clear')
            def banner():
                MAGENTE(r''' 
                __________________  ___________     ___________ _______  ________________________.___.__________________________________________ 
                \______   \______ \ \_   _____/     \_   _____/ \      \ \_   ___ \______   \__  |   |\______   \__    ___/\_   _____/\______   \
                |     ___/|    |  \ |    __)        |    __)_  /   |   \/    \  \/|       _//   |   | |     ___/ |    |    |    __)_  |       _/
                |    |    |    `   \|     \         |        \/    |    \     \___|    |   \\____   | |    |     |    |    |        \ |    |   \
                |____|   /_______  /\___  /        /_______  /\____|__  /\______  /____|_  // ______| |____|     |____|   /_______  / |____|_  /
                                \/     \/                 \/         \/        \/       \/ \/                                    \/         \/ 
            ''')
            banner()
            print('\u001b[35meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
            try:
                pdf = input("\u001b[35m[+] Enter the PDF you want to decrypt: ")
                time.sleep(2)
                openwith = open(pdf, "rb")
                pdfreader = PyPDF2.PdfFileReader(pdf)
                question = input("\u001b[35m[+] Does your PDF contain a password(yes/no): ")
                time.sleep(2)
                if question == "no":
                    print("\033[91m[-] Use the PDF reader at section number 5 dummy.....................")
                    exit()
                password = str(input("\u001b[35m[+] Enter your password: "))
                time.sleep(2)
                pdfreader.decrypt(password)
                pages = input("\u001b[35m[+] Do you want to know how many pages your PDF contains?(yes/no): ")
                time.sleep(2)
                if pages == "no":
                    print("\033[91mDon't press the keyboard so hardly or else your will break it.............")
                else:
                    print("\033[91m[-] Counting pages...................")
                    time.sleep(2)
                    print("\033[91m[-] Your pdf has", pdfreader.numPages, "pages")
                time.sleep(2)
                page = int(input("\u001b[35m[+] Enter the page you want to read: "))
                read = pdfreader.getPage(page)
                print(read.extractText())
            except:
                print("\033[91m[+] Use the right choice of word young one!!!!!!!")
        if choose == "3":
            os.system('clear')
            def banner():
                BLUE(r'''
        
                                _____   ____ ___________  .___________ __________ ________   ________   ____  __.
                                /  _  \ |    |   \______ \ |   \_____  \\______   \\_____  \  \_____  \ |    |/ _|
                                /  /_\  \|    |   /|    |  \|   |/   |   \|    |  _/ /   |   \  /   |   \|      <  
                                /    |    \    |  / |    `   \   /    |    \    |   \/    |    \/    |    \    |  \ 
                                \____|__  /______/ /_______  /___\_______  /______  /\_______  /\_______  /____|__ \
                                        \/                 \/            \/       \/         \/         \/        \/
            ''')
            banner()
            print("\u001b[34m///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
            pdf = input("\u001b[34m[+] Enter your pdf: ")
            pdfreader = PyPDF2.PdfFileReader(pdf)
            listen = int(input("\u001b[34m[+] At which page do you wish to start: "))
            print("\u001b[34m[-] Loading Audiobook...........")
            print("\u001b[34m[-] Audiobook Loading...............")
            print("\u001b[34m[-] Audiobook has started...................")
            page = pdfreader.numPages
            speaker = pyttsx3.init()
            for pageNum in range(listen, page):
                page = pdfreader.getPage(listen)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()
        if choose == "5":
            os.system('clear')
            def banner():
                GREEN(r'''
            __________________  ___________     _____________________   _____  ________  _____________________ 
            \______   \______ \ \_   _____/     \______   \_   _____/  /  _  \ \______ \ \_   _____/\______   \
            |     ___/|    |  \ |    __)        |       _/|    __)_  /  /_\  \ |    |  \ |    __)_  |       _/
            |    |    |    `   \|     \         |    |   \|        \/    |    \|    `   \|        \ |    |   \
            |____|   /_______  /\___  /         |____|_  /_______  /\____|__  /_______  /_______  / |____|_  /
                            \/     \/                 \/        \/         \/        \/        \/         \/ 
            ''')
            banner()
            print('\033[92m]rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
            file = input("\033[92m][+] Enter the pdf you want to read: ")
            open = open(file, "rb")
            pdfreader = PyPDF2.PdfFileReader(file)
            read = int(input("[+] Enter the page you want to read: "))
            pages = pdfreader.numPages
            page = pdfreader.getPage(read)
            text = page.extractText()
            print(text)
        if choose == "6":
            os.system('clear')
            os.close()
    except:
        print("\033[91m[-] Invalid input!!!!!")
        continue
    



