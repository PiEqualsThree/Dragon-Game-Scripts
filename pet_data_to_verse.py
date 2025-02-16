import csv

baseColumnIdx = 0
nameColumnIdx = 1
rarityColumnIdx = 2
dropWeightColumnIdx = 3
powerColumnIdx = 4
expressionColumnIdx = 5
oddsColumnIdx = 6

def main():
    with open('PetData.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        rows = list(reader)
        with open('pet_data.txt', 'w') as txtFile:
            for row in rows:
                txtFile.write(f"\"{row[nameColumnIdx]}\" => pet_data:\n")
                txtFile.write(f"    Power := {row[powerColumnIdx]}\n")
                txtFile.write(f"    PetName := \"{row[nameColumnIdx]}\"\n")
                txtFile.write(f"    PetMesh := PetAssets.{row[baseColumnIdx][:-2]}.{row[baseColumnIdx]}.{row[baseColumnIdx]}\n")
                txtFile.write(f"    FaceTexture := PetAssets.{row[baseColumnIdx][:-2]}.{row[baseColumnIdx].lower()}_face\n")
                txtFile.write(f"    ExpressionTexture := PetAssets.Expressions.{row[expressionColumnIdx]}\n")
                txtFile.write(f"    RarityData := pet_rarity_data:\n        RarityTier := pet_rarity.{row[rarityColumnIdx]}\n        RarityWeight := {row[dropWeightColumnIdx]}\n        RarityString := \"1 in {row[oddsColumnIdx]}\"\n\n")
                



main()



# "Prism"=>pet_data:
#         Power := 8
#         PetName := "Prism"
#         PetMesh := PetAssets.Diamond.Diamond_1.Diamond_1
#         FaceTexture := PetAssets.Diamond.diamond_1_face
#         ExpressionTexture := PetAssets.Expressions.Angry
#         RarityData := pet_rarity_data:
#             RarityTier := pet_rarity.Rare
#             RarityWeight := 100



# "Terra"=>pet_data:
#     Power := 5
#     PetName := "Terra"
#     PetMesh := PetAssets.Earth.Earth_1.Earth_1
#     FaceTexture := PetAssets.Earth.earth_1_face
#     ExpressionTexture := PetAssets.Expressions.Unibrow
#     RarityData := pet_rarity_data:
#         RarityTier := pet_rarity.Common
#         RarityWeight := 150