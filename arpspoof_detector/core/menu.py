class Menu:
    def __init__(self):
        print('''
   ____                           __               ___    ___   ___ 
  /  _/___   ___  ___  ___  ____ / /_ ___   ____  / _ |  / _ \ / _ \\
 _/ / / _ \ (_-< / _ \/ -_)/ __// __// _ \ / __/ / __ | / , _// ___/ 
/___//_//_//___// .__/\__/ \__/ \__/ \___//_/   /_/ |_|/_/|_|/_/
               /_/
    ''')
        print('\033[33m+' + '-' * 23 + '+\n'
              '|     Select System     |\n' 
              '+' + '-' * 23 + '+\033[0m')

        print('\033[32m1) Linux\033[0m')
        print('\033[31m2) macOS\033[0m')
        print('\033[34m3) Windows\033[0m')
        print('*) Help')