data= {
    'PYTHON20201':['ALFRED',0],
    'PYTHON20202':['VICTOR',0],
    'PYTHON20203':['ELIJAH',0],
    'PYTHON20204':['DAVID E',0],
    'PYTHON20205':['DAVID P',0],
    'PYTHON20206':['MARYAM',0],
    'MATRICINEC':['INEC',0]
}
candidates= {
     'MARYAM':['cand1',0],
   'DAVID E' :['cand2',0]
}    
maryam = candidates['MARYAM'][1]
david_e = candidates['DAVID E'][1]

vote_period = 'open'
while vote_period=='open':
    mat= input('enter matric number ')
    voter_mat= mat.upper()
    if voter_mat in data or voter_mat=='MATRICINEC':
        if data[voter_mat][1]==0:
            vote= input(f'''
            vote for your choice using:
            cand1
            cand2
            ''')
            if vote == candidates['MARYAM'][0]:
                print('vote was successful')
                maryam = maryam + 1
                data[voter_mat][1] = 1
            elif vote == candidates['DAVID E'][0]:
                print('vote was successful')
                david_e = david_e + 1
                data[voter_mat][1] = 1
            elif vote =='INEC2020': # close or keep voting period open
                vote_period = 'closed'

                # Compute results
                print(f"""
                VOTING RESULTS
                =======================
                MARYAM: {maryam} votes
                DAVID: {david_e} votes
                """)
                if maryam > david_e:
                    print(f'Maryam wins with {maryam} votes')
                else:
                    print(f'David wins with {david_e} votes')
            else:
                print('vote wasn\'t successful')
        else:
            print('you have voted before')
    else:
        print('please you are not allowed')
input()
