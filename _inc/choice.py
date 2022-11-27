def user_choice():
    while True:
        inp = input('[HUMAN]Choose youqr mark[x/o]: ')
        if inp in ['x' , 'X']:
            print('[HUMAN]You choose "X".\n[HUMAN]You play first.')
            return 'x','o'
        elif inp in ['O','o']:
            print('[HUMAN] You choose "O".\n[HUMAN] Computer plays first.')
            return 'o','x'
        else:
            print('[HUMAN] Enter correct input!')