print('\n Welcome to EssayHelp!')
while True:
    try:
       price = {'Essay': 12, 'Report':14, 'Thesis': 19} 
       print('\n1. Essay \n2. Report \n3. Thesis')
       option = int(input('\nSelect option e.g. 1 for essay: \n '))
       pages = int(input('number of pages: \n '))  
          
       if option == 1:        
           print('\nTotal Order Value:', '$', pages * price['Essay'])
           print('Your essay assignment has been received. ')
       if option == 2:  
           print('\nTotal Order Value:', '$', pages * price['Report'])           
           print('Your report assignment has been received.')
       if option == 3:
           print('\nTotal Order Value:', '$', pages * price['Thesis'])
           print('Your thesis assignment has been received. ')
    except ValueError as err:
        print('\nInvalid value. ')
    finally:
       exit()