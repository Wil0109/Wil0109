listStudentData= [
    {
        'Student ID':'1A',
        'Name':'Andri',
        'Age':20,
        'Gender': 'M',
        'Score':74,
        'Grade':'C'
    },
    {
        'Student ID':'1B',
        'Name':'Budi',
        'Age':23,
        'Gender': 'M',
        'Score':84,
        'Grade':'B'
    },
    {
        'Student ID':'1C',
        'Name':'Citra',
        'Age':21,
        'Gender': 'F',
        'Score':35,
        'Grade':'Failed'
    }
]

def yakinchecker():
    while True:
        yakinChecker=(input('Are you sure?(Y/N): ')).upper() #Apakah Anda yakin?
        if yakinChecker == 'Y':
            return "Y"
        elif yakinChecker =="N":
            return 'N'
        else:
            print('< Please choose between Y or N letter only, "Y" for yes and "N" for no >')
            continue 

def exitornot():
    while True:
        exitornot=(input('Would you like to exit the program and return to the main menu (y/n):')).upper()
        if exitornot == 'N':
            return 'N'
        elif exitornot == 'Y':
            return 'Y'
        else:
            print('< Please choose between Y or N letter only, "Y" for yes and "N" for no >')

def menampilkanStudentData():
    print('_'*97+'\n')
    print('\nStudent Data Report:')
    print('='*97+'\n')
    print('|Index:\t| Student ID:\t| Name:\t\t| Age:\t| Gender (M/F):\t| Score:\t| Grade:\t|')
    print('-'*97)
    for i in range(len(listStudentData)):
            print('|{:2}\t| {:12}\t| {:10}\t| {}\t| {:12}\t| {}\t\t| {:12}\t|'.format(i,listStudentData[i]['Student ID'],listStudentData[i]['Name'],listStudentData[i]['Age'],listStudentData[i]['Gender'],listStudentData[i]['Score'],listStudentData[i]['Grade']))
    print('\n'+'='*97+'\n')

def failedStudentlist(listStudentData):
    students_with_failed_grade = []
    for i,student in enumerate(listStudentData):
        grade = student['Grade']
        if grade == 'Failed':
            students_with_failed_grade.append((i,student))
    return students_with_failed_grade

def sortingStudentData():
    while True:
                others = (input('''                        
===== Online School ABC Student Data Records =====
                        
        Sorting Features:
        1. Student Ranking (Grades)
        2. Alphabetically 
        3. Failed Students
        4. Keluar
                        
        Please Choose Main Menu Option [1-4]:'''))
                print('\n')
                if(others == "1"):
                    print('_'*97+'\n')
                    print('\n1. Student Ranking (Grades): \n')
                    print('='*97+'\n')
                    print('|Index:\t| Student ID:\t| Name:\t\t| Age:\t| Gender (M/F):\t| Score:\t| Grade:\t|')
                    for i in range(len(listStudentData)):
                        listStudentData.sort(key=lambda listStudentData:listStudentData['Score'],reverse=True)
                        print('|{:2}\t| {:12}\t| {:10}\t| {}\t| {:12}\t| {}\t\t| {:12}\t|'.format(i,listStudentData[i]['Student ID'],listStudentData[i]['Name'],listStudentData[i]['Age'],listStudentData[i]['Gender'],listStudentData[i]['Score'],listStudentData[i]['Grade']))
                        i += 1
                    print('\n'+'='*97+'\n')
                    
                elif(others=='2'):
                    print('_'*97+'\n')
                    print('\n2. Students Alphabetic Order: \n')
                    print('='*97+'\n')
                    print('|Index:\t| Student ID:\t| Name:\t\t| Age:\t| Gender (M/F):\t| Score:\t| Grade:\t|')
                    for i in range(len(listStudentData)):
                        listStudentData.sort(key=lambda listStudentData:listStudentData['Name'])
                        print('|{:2}\t| {:12}\t| {:10}\t| {}\t| {:12}\t| {}\t\t| {:12}\t|'.format(i,listStudentData[i]['Student ID'],listStudentData[i]['Name'],listStudentData[i]['Age'],listStudentData[i]['Gender'],listStudentData[i]['Score'],listStudentData[i]['Grade']))
                        i += 1
                    print('\n'+'='*97+'\n')

                elif(others=='3'):
                    print('_'*97+'\n')
                    print('\n 3. Students Who Failed: \n')
                    print('='*97+'\n')
                    print('|Index:\t| Student ID:\t| Name:\t\t| Age:\t| Gender (M/F):\t| Score:\t| Grade:\t|')
                    failedStudentlist(listStudentData)
                    students_with_failed_grade = failedStudentlist(listStudentData)
                    for index, student in students_with_failed_grade:
                        print('|{:2}\t| {:12}\t| {:10}\t| {}\t| {:12}\t| {}\t\t| {:12}\t|'.format(index,student['Student ID'], student['Name'], student['Age'], student['Gender'], student['Score'], student['Grade']))

                elif(others=='4'):
                    print('_'*97+'\n')
                    print('\n< Exitting the Sorting programme and going back to the main menu. >\n')
                    print('_'*97+'\n')
                    break
                else:
                    print('_'*97+'\n')
                    print('< Sorry, the option you have chosen is not found. Please retry.>')
                    print('_'*97+'\n')
                    continue

def menambahStudentData(): 
    menampilkanStudentData()
    while True:
        print('\nAdding New Student Data: \n')
        newStudentID= (input('New Student ID: ')).upper()
        newStudentName= (input('New Student Name: ')).capitalize()
        try:
            newStudentAge= int(input('New Student Age: ')) 
            if newStudentAge <=0:
                  print('< Age cannot be 0 or under >')
                  continue 
        except ValueError:
            print('< Please only use digits for age. >')
            continue
        while True:
            newStudentGender= ((input('New Student Gender (Please choose "M"/"F"): '))).upper()
            if newStudentGender.upper() == 'M' or newStudentGender.upper() =='F':
                break
            else:
                print( '< Please only use "M/"F" ("M" for Male or "F" for Female) >')
                continue
        newStudentScore= float(input('New Student Score: '))
        newStudentScore= int(newStudentScore)
        newStudentGrade= ''
        if(newStudentScore >=90 and newStudentScore <= 100):
            newStudentGrade= 'A'
        elif(newStudentScore >=85 and newStudentScore <90):
            newStudentGrade= 'A-'
        elif(newStudentScore >=80 and newStudentScore <85):
            newStudentGrade= 'B'
        elif(newStudentScore >=75 and newStudentScore <80):
            newStudentGrade= 'B-'
        elif(newStudentScore >=70 and newStudentScore <75):
            newStudentGrade= 'C'
        elif(newStudentScore >=65 and newStudentScore <70):
            newStudentGrade= 'C-'
        elif(newStudentScore >=0 and newStudentScore <65):
            newStudentGrade= 'Failed'
        elif(newStudentScore>100):
            print('\n< We do not accept scores above 100. >')
            print('< Please Retry >\n\n')
            continue
        else:
            print('\n< Negative numbers, special characters and letters are not accepted in this input. >')
            print('< Please Retry >\n\n')
            continue
        yakincheck= yakinchecker()
        exitcheck= exitornot()
        if yakincheck == 'N' and exitcheck == 'N':
            print('< Continuing the Adding Program >')
            print('_'*97+'\n')
            continue
        elif yakincheck == 'Y' and exitcheck == 'Y':
            listStudentData.append({
            'Student ID': newStudentID,
            'Name': newStudentName,
            'Age': newStudentAge,
            'Gender': newStudentGender,
            'Score': newStudentScore,
            'Grade': newStudentGrade
        })
            menampilkanStudentData()
            print('< Student Successfully Added >')
            print('< You will now be returning to the Main Menu. >')
            print('_'*97+'\n')
            return
        elif yakincheck == 'Y' and exitcheck == 'N':
            listStudentData.append({
            'Student ID': newStudentID,
            'Name': newStudentName,
            'Age': newStudentAge,
            'Gender': newStudentGender,
            'Score': newStudentScore,
            'Grade': newStudentGrade
        })
            menampilkanStudentData()
            print('< Student Successfully Added >')
            print('< Continuing the Adding Program >')
            print('_'*97+'\n')
            continue
        elif yakincheck == 'N' and exitcheck == 'Y':
            print('< You will now be returning to the Main Menu. >')
            print('_'*97+'\n')
            return

def menggantiStudentData():
    while True:
        menampilkanStudentData()
        try:
            indexDictContoh=int(input('Enter the Student Index that wants to be Updated:')) #Massukan index Student yang ingin diganti
        except ValueError:
            print('< Please only use digits. >')
            continue
        Ganti=(input('''                 
===== Online School ABC Student Data Records =====
                        
        What do you want to change:
        1. Student ID
        2. Name 
        3. Age
        4. Gender
        5. Score
        6. Exit ( If you have finished or want to cancel updatting)
                        
        Please Choose Main Menu Option [1-6]:'''))
        print('\n')
        if Ganti == '1':
            temp_value = listStudentData[indexDictContoh]['Student ID']
            listStudentData[indexDictContoh]['Student ID'] = input('Place your Change in Student ID:').upper()
            yakincheck = yakinchecker()
            if yakincheck == 'N':
                listStudentData[indexDictContoh]['Student ID'] = temp_value
        elif Ganti == '2':
            temp_value = listStudentData[indexDictContoh]['Name']
            listStudentData[indexDictContoh]['Name'] = input('Place your Change in Name:').capitalize()
            yakincheck = yakinchecker()
            if yakincheck == 'N':
                listStudentData[indexDictContoh]['Name'] = temp_value
        elif Ganti == '3':
            temp_value = listStudentData[indexDictContoh]['Age']
            try:
              listStudentData[indexDictContoh]['Age'] = int(input('Place your Change in Age:'))
              if listStudentData[indexDictContoh]['Age'] <= 0:
                  print('< Age cannot be 0 or under >')
                  continue
            except ValueError:
              print('< Please only use digits for age. >')
              continue
            if yakincheck == 'N':
                listStudentData[indexDictContoh]['Age'] = temp_value
        elif Ganti == '4':
            temp_value = listStudentData[indexDictContoh]['Gender']
            while True:
                listStudentData[indexDictContoh]['Gender'] = input('Place your Change in Gender (f/m):').upper()
                if listStudentData[indexDictContoh]['Gender'] == 'M' or listStudentData[indexDictContoh]['Gender'] =='F':
                    break
                else:
                    print( '< Please only use "M/"F" ("M" for Male or "F" for Female) >')
                    continue
            if yakincheck == 'N':
                listStudentData[indexDictContoh]['Gender'] = temp_value
        elif Ganti == '5':
            temp_value = listStudentData[indexDictContoh]['Score']
            listStudentData[indexDictContoh]['Score'] = int(input('Place your Change in Score:'))
            if yakinchecker() == 'N':
                listStudentData[indexDictContoh]['Score'] = temp_value
            if(listStudentData[indexDictContoh]['Score'] >=90 and listStudentData[indexDictContoh]['Score'] <= 100):
                    changetudentGrade= 'A'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=85 and listStudentData[indexDictContoh]['Score'] <90):
                    changetudentGrade= 'A-'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=80 and listStudentData[indexDictContoh]['Score'] <85):
                    changetudentGrade= 'B'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=75 and listStudentData[indexDictContoh]['Score'] <80):
                    changetudentGrade= 'B-'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=70 and listStudentData[indexDictContoh]['Score'] <75):
                    changetudentGrade= 'C'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=65 and listStudentData[indexDictContoh]['Score'] <70):
                    changetudentGrade= 'C-'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score'] >=0 and listStudentData[indexDictContoh]['Score'] <65):
                    changetudentGrade= 'Failed'
                    listStudentData[indexDictContoh]['Grade'] = changetudentGrade
            elif(listStudentData[indexDictContoh]['Score']>100):
                    print('\n< We do not accept scores above 100. >')
                    print('< Please Retry >\n\n')
                    continue
            else:
                print('\n< Negative numbers, special characters and letters are not accepted in this input. >')
                print('< Please Retry >\n\n')
                print('_'*97+'\n')
                continue
        elif Ganti == '6':
            print('\n< Exitting the Updating programme and going back to the main menu. >\n')
            print('_'*97+'\n')
            break
        else:
            print('< Sorry, the option you have chosen is not found. Please retry.>')
            print('_'*97+'\n')
            continue

        exitcheck= exitornot()
        if yakincheck == 'N' and exitcheck == 'N':
            print('< Continuing the Updating Program >') 
            print('_'*97+'\n')
            continue
        elif yakincheck == 'Y' and exitcheck == 'Y':
            menampilkanStudentData()
            print('< Student Successfully Updated >')
            print('< You will now be returning to the Main Menu. >')
            print('_'*97+'\n')
            return
        elif yakincheck == 'Y' and exitcheck == 'N':
            menampilkanStudentData()
            print('< Student Successfully Updated >')
            print('< Continuing the Updating Program >')
            print('_'*97+'\n')
            continue
        elif yakincheck == 'N' and exitcheck == 'Y':
            print('< You will now be returning to the Main Menu. >')
            print('_'*97+'\n')
            return
        
def menghapusStudentData():
    while True:
        menampilkanStudentData()
        try:
            indexStudentDelete=int(input('Which student index would you like to delete:'))
        except ValueError:
              print('< Please only use digits. >')
              continue
        yakincheck= yakinchecker()
        exitcheck= exitornot()
        if yakincheck == 'N' and exitcheck == 'N':
            print('< Continuing the Deleting Program >')
            print('_'*97+'\n')
            continue
        elif yakincheck == 'Y' and exitcheck == 'Y':
            del listStudentData[indexStudentDelete]
            menampilkanStudentData()
            print('< Student Successfully Deleted >')
            print('< You will now be returning to the main menu. >')
            print('_'*97+'\n')
            return
        elif yakincheck == 'Y' and exitcheck == 'N':
            del listStudentData[indexStudentDelete]
            menampilkanStudentData()
            print('< Student Successfully Deleted >')
            print('< Continuing the Deleting Program >')
            print('_'*97+'\n')
            continue
        elif yakincheck == 'N' and exitcheck == 'Y':
            print('< You will now be returning to the main menu. >')
            print('_'*97+'\n')
            return
     
while True:
# Main Menu Loop
        pilihanMainMenu = input('''
                       
===== Online School ABC Student Data Records =====
                        
List Menu:
1. View Student Data Report and Grades
2. Add Student Data
3. Edit Student Data
4. Delete Student Data
5. Exit Program
                        
Please Choose Main Menu Option [1-5]: ''')
        
        if(pilihanMainMenu=='1'):
            menampilkanStudentData()
            sortingStudentData()
        elif(pilihanMainMenu=='2'):
            menambahStudentData()
        elif(pilihanMainMenu=='3'):
            menggantiStudentData()
        elif(pilihanMainMenu=='4'):
            menghapusStudentData()
        elif(pilihanMainMenu=='5'):
            print('\n < Thank you, you have successfully exit the programme! >\n')
            break
        else:
            print('\n < Sorry, the option you have chosen is not found. Please retry.>\n')
            continue