import random
import math
import csv
import json

baseColumnIdx = 0
nameColumnIdx = 1
rarityColumnIdx = 2
dropWeightColumnIdx = 3
powerColumnIdx = 4
expressionColumnIdx = 5
oddsColumnIdx = 6

totalCommonWeight = 0
totalUncommonWeight = 0
totalRareWeight = 0
totalEpicWeight = 0
totalLegendaryWeight = 0

rarityWeights = {
    "Common" : 7500000,
    "Uncommon" : 150000,
    "Rare" : 15000,
    "Epic" : 2000,
    "Legendary" : 50,
    "Mythic" : 2
}

rarityOddsDenominators = {
    "Common" : 1,
    "Uncommon" : 1,
    "Rare" : 1,
    "Epic" : 1,
    "Legendary" : 1,
    "Mythic" : 1
}

petOdds = {
    "Common" :    { "totalWeight" : 0, "petOdds": {}},
    "Uncommon" :  { "totalWeight" : 0, "petOdds": {}},
    "Rare" :      { "totalWeight" : 0, "petOdds": {}},
    "Epic" :      { "totalWeight" : 0, "petOdds": {}},
    "Legendary" : { "totalWeight" : 0, "petOdds": {}},
    "Mythic" :    { "totalWeight" : 0, "petOdds": {}},
}

def main():
    with open('PetData.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        title = next(reader)
        rows = list(reader)
        print(rows)
        modifyRowDropWeights(rows)
        calculateRarityOdds()
        calculatePetOdds(rows)

        with open('new_pet_data.csv', 'w', newline="") as newFile:
            writer = csv.writer(newFile)
            writer.writerow(title)
            for row in rows:
                print("Row stuff")
                petRarityOdds = rarityOddsDenominators[row[rarityColumnIdx]]
                petIndividualOdds = petOdds[row[rarityColumnIdx]]["petOdds"][row[nameColumnIdx]]
                petTotalOdds = normalizeDropOdds(petRarityOdds * petIndividualOdds)
                row[oddsColumnIdx] = petTotalOdds
                writer.writerow(row)  


def calculatePetOdds(rows):
    # Calculate totals 
    for row in rows:
        petOdds[row[rarityColumnIdx]]["totalWeight"] += int(row[dropWeightColumnIdx])

    # Calculate pet odds
    for row in rows:
        petName = row[nameColumnIdx]
        petDropOdds = math.floor(petOdds[row[rarityColumnIdx]]["totalWeight"] / int(row[dropWeightColumnIdx]))
        petDropOdds = petDropOdds
        petOdds[row[rarityColumnIdx]]["petOdds"][petName] = petDropOdds

    print(petOdds)


def calculateRarityOdds():
    totalWeight = 0
    for rarity, weight in rarityWeights.items():
        totalWeight += weight
    print(f"Total weight: {totalWeight}")

    for rarity, weight in rarityWeights.items():
        odds = max(math.floor(totalWeight / weight), 2)
        rarityOddsDenominators[rarity] = odds
        print(f"Rarity {rarity} has 1 in {odds} odds!")        

def modifyRowDropWeights(rows):
    for row in rows:
        if row[rarityColumnIdx] == "Common":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(1, 9), random.randint(10, 15)))

        elif row[rarityColumnIdx] == "Uncommon":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(1, 15), random.randint(20, 40)))

        elif row[rarityColumnIdx] == "Rare":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(1, 20), random.randint(25, 100)))

        elif row[rarityColumnIdx] == "Epic":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(1, 30), random.randint(35, 300)))

        elif row[rarityColumnIdx] == "Legendary":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(1, 45), random.randint(55, 750)))

        elif row[rarityColumnIdx] == "Mythic":
            row[dropWeightColumnIdx] = str(random.randint(random.randint(0, 80), random.randint(150, 1000)))

def normalizeDropOdds(dropOdd):
    if dropOdd > 19:
        tenths = math.floor(math.log10(dropOdd))
        roundFactor = max(5 * math.pow(10, tenths - 2), 5)
        normalizedValue = roundFactor * math.floor(dropOdd / roundFactor)
        return normalizedValue
    else:
        return dropOdd


def test():
    pass

def formatInt(Number):
    if Number < 1000: return Number


main()