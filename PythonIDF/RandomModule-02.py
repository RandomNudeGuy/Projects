import random

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

def LuckyRoll(NumList):
    Nums = random.choices(NumList, k = 3)
    for i in Nums:
        if i == 7:
            return True
        else:
            for i in range(0, len(NumList)):
                total = total + NumList[i]
            if total == 7:
                return True
            else:
                return False

# NumList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
