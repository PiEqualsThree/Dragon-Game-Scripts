import random
import math
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
totalEpicWeight = 0
totalLegendaryWeight = 0

rarityWeights = {
    "Common" : 5000000,
    "Uncommon" : 1000000,
    "Rare" : 25000,
    "Epic" : 2000,
    "Legendary" : 10,
    "Mythic" : 1
}

rarityOddsDenominators = {
    "Common" : 1,
    "Uncommon" : 1,
    "Rare" : 1,
    "Epic" : 1,
    "Legendary" : 1,
    "Mythic" : 1
}

petRarityTotalWeights = {
    "Common" : 1,
    "Uncommon" : 1,
    "Rare" : 1,
    "Epic" : 1,
    "Legendary" : 1,
    "Mythic" : 1
}

commonPetOddsDeonimators = {}
uncommonPetOddsDeonimators = {}
rarePetOddsDeonimators = {}
epicPetOddsDeonimators = {}
LegendaryPetOddsDeonimators = {}
MythicPetOddsDeonimators = {}


def main():
    with open('DragonPetData.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        title = next(reader)
        calculateRarityOdds()

        # with open('PetData.csv', 'w', newline="") as newFile:
        #     writer = csv.writer(newFile)
        #     writer.writerow(title)
        #     for row in reader:
        #         modifyRowDropWeight(row)
        #         writer.writerow(row)  

def calculateRarityOdds():
    totalWeight = 0
    for rarity, weight in rarityWeights.items():
        totalWeight += weight
    print(f"Total weight: {totalWeight}")

    for rarity, weight in rarityWeights.items():
        odds = max(math.floor(totalWeight / weight), 2)
        rarityOddsDenominators[rarity] = odds
        print(f"Rarity {rarity} has 1 in {odds} odds!")        

def calculatePetOdds(petrows, rarity):
    pass

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