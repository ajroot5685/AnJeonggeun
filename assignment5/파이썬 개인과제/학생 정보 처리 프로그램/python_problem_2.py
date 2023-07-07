#함수 이름은 변경 가능합니다.

studentlist=[]
middlescore={}
finalscore={}
gradelist={}

##############  menu 1
def Menu1(name, mid, final) :
    #사전에 학생 정보 저장하는 코딩 
    studentlist.append(name)
    middlescore[name]=mid
    finalscore[name]=final

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for student in studentlist:
        if student not in gradelist:
            mid=middlescore[student]
            final=finalscore[student]
            cal=(mid+final)/2
            if cal>=90:
                gradelist[student]='A'
            elif cal>=80:
                gradelist[student]='B'
            elif cal>=70:
                gradelist[student]='C'
            else:
                gradelist[student]='D'

##############  menu 3
def Menu3() :
    #출력 코딩
    print()
    print('---------------------------')
    print('name\tmid\tfinal\tgrade')
    print('---------------------------')
    for student in studentlist:
        print(student, middlescore[student], finalscore[student], gradelist[student], sep='\t')

##############  menu 4
def Menu4(name):
    #학생 정보 삭제하는 코딩
    try:
        del gradelist[name]
    except:
        None
    del finalscore[name]
    del middlescore[name]
    studentlist.remove(name)

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        input_list=[]
        input_list=input("Enter name mid-score final-score : ").split()
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)

        if len(input_list)!=3:
            print("Num of data is not 3!")
            continue
        if input_list[0] in studentlist:
            print('Already exist name!')
            continue
        try:
            score1=int(input_list[1])
            score2=int(input_list[2])
        except ValueError:
            print('Score is not positive integer!')
            continue
        if score1<=0 or score2 <= 0:
            print('Score is not positive integer!')
            continue
        
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        Menu1(input_list[0], score1, score2)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(studentlist)==0:
            print('No student data!')
            continue
        #예외사항이 아닌 경우 2번 함수 호출
        Menu2()
        #"Grading to all students." 출력
        print("Grading to all students.")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if len(studentlist)==0:
            print('No student data!')
            continue
        if len(studentlist)!=len(gradelist):
            print('There is a student who didn\'t get grade.')
            continue
        #예외사항이 아닌 경우 3번 함수 호출
        Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if len(studentlist)==0:
            print('No student data!')
            continue
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        delete_name=input('Enter the name to delete : ')
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        if delete_name not in studentlist:
            print('Not exist name!')
            continue
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        Menu4(delete_name)
        print(delete_name,'student information is deleted.')

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print('Exit Program!')
        #반복문 종료
        break

    else :
        print("Wrong number. Choose again.")