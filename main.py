import random
import csv

baseColumnIdx = 0
nameColumnIdx = 1
rarityColumnIdx = 2
dropWeightColumnIdx = 3
powerColumnIdx = 4
expressionColumnIdx = 5

totalCommonWeight = 0
totalUncommonWeight = 0
totalRareWeight = 0


def main():
    with open('DragonPetData.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        title = next(reader)
        with open('PetData.csv', 'w', newline="") as newFile:
            writer = csv.writer(newFile)
            writer.writerow(title)
            for row in reader:
                modifyRowDropWeight(row)
                writer.writerow(row)
                
        

def modifyRowDropWeight(row):
    if row[rarityColumnIdx] == "Common":
        row[dropWeightColumnIdx] = str(random.randint(40, 100))

    elif row[rarityColumnIdx] == "Uncommon":
        row[dropWeightColumnIdx] = str(random.randint(15, 110))

    elif row[rarityColumnIdx] == "Rare":
        row[dropWeightColumnIdx] = str(random.randint(10, 150))

    elif row[rarityColumnIdx] == "Epic":
        row[dropWeightColumnIdx] = str(random.randint(10, 200))

    elif row[rarityColumnIdx] == "Legendary":
        row[dropWeightColumnIdx] = str(random.randint(1, 300))

    elif row[rarityColumnIdx] == "Mythic":
        row[dropWeightColumnIdx] = str(random.randint(1, 1000))



main()