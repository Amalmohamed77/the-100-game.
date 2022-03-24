 #welcome message to the players.

print("** hello, welcome to the 100 game **")
print("player1 name:")
num1 = input("please,enter your name:") #player1 name.
print("welcome:",num1)
print("player2 name:")
num2 = input("please,enter your name:") #player2 name.
print("welcome:",num2)
main_list=["1","2","3","4","5","6","7","8","9","10"] #the numburs which the players can use only.
print("each players has only the numbers:",main_list)
player1=[1,2,3,4,5,6,7,8,9,10]
player2=[1,2,3,4,5,6,7,8,9,10]
a=1
sum1=0
sum2=0
total_score=0
if total_score < 100:
    while a <=10:
        turn1 = int(input ( "player1:please, choose number:"))# turn to player1 to choose.
        if turn1 <= 0:
            print("please,enter a positive number from 1:10")
        elif turn1 > 0 and turn1 <= 10:
            for i in player1:
                if i == turn1:
                    player1.remove(turn1)
                    # remove the num which the player select before.
                    print(num1 + (" Your available numbers are now:") + str(player1))
                    # print amessag for the player to know his avaliable numbers.


            sum1 += turn1
            total_score += turn1
            print("total number that " + num1 + " scored is:" + str(sum1))
            print("total score now is: " + str(total_score))
            if total_score == 100:  # the winning case.
                print(num1, "***congratulation,you win***")

            if total_score > 100:  # when entered invalid number cause the total over than 100.
                print("oops", num1, "the total score is over 100 now --")
                print("game over")

            turn2 = int(input("player2:please, choose number:"))
            for x in player2:
                if x == turn2:
                    player2.remove(turn2)
                    print(num2 + (" Your available numbers are now:") + str(player2))

            sum2 += turn2
            print("total number that " + num2 + " scored is:" + str(sum2))
            total_score += turn2  # the total score which they entered
            print("total score now is: " + str(total_score))
            if total_score == 100:  # the winning case.
                print(num2, "***congratulation,you win***")

            if total_score > 100:  # when entered invalid number cause the total over than 100.
                print("oops", num2, "the total score is over 100 now --")
                print("game over")

            a += 1
           