import random
import time

#$First Question
#% firstNum = int(input("Enter first num:"))
#% secondNum = int(input("Enter second num:"))

#% randomnum = random.randrange(firstNum, secondNum + 1)

#% print(randomnum)

#$Second Question

#% numList = []

#% for i in range(10):
#%     num = int(input("Enter Num:"))
#%     numList.append(num)

#% RollOverNum = int(input("Enter RollOver:"))

#% print(random.choices(numList, k = RollOverNum))

#$Third Question

#% def DiceRoll(DiceList):

#%     result = random.choices(DiceList, k = 2)
#%     return result

#% DiceList = [1, 2, 3, 4, 5, 6]

#% print(DiceRoll(DiceList))

#$Fourth Question

#% def LuckyRoll(NumList):
#%     total = 0
#%     Nums = random.choices(NumList, k = 3)
#%     for i in Nums:
#%         if i == 7:
#%             print(Nums)
#%             return True
#%         else:
#%             for i in range(0, len(NumList)):
#%                 total = total + NumList[i]
#%             if total == 7:
#%                 print(Nums)
#%                 return True
#%             else:
#%                 print(Nums)
#%                 return False

#% NumList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#% print(LuckyRoll(NumList))

#$Fifth Question

#% def four_DiceRoll(Dice):
#%     total = 0
#%     for i in range(4):
#%         result = random.choice(Dice)
#%         time.sleep(1)
#%         total = total + result
#%         print(result)
#%     return total


#% DiceList = [1, 2, 3, 4, 5, 6]
#% print(four_DiceRoll(DiceList))

#$Sixth Question

#% def two_numroll():
#%     NumRoll1 = random.randrange(10, 101, 2)
#%     NumRoll2 = random.randrange(10, 101, 2)

#%     if NumRoll1 > NumRoll2:
#%         msg = f"Num1 > {NumRoll1}, is bigger than Num2 > {NumRoll2}"
#%         return msg
#%     elif NumRoll2 == NumRoll1:
#%         msg = f"Nums are even. {NumRoll1} == {NumRoll2}"
#%         return msg
#%     else:
#%         msg = f"Num2 > {NumRoll2}, is bigger than Num1 > {NumRoll1}"
#%         return msg
    
#% print(two_numroll())

#$Seventh Question


    