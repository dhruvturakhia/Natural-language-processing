from gensim.models import Word2Vec, KeyedVectors


def classDistances(model, dictionary):
    distances = {"inclass": {}, "betweenclass": {}}
    listkeys = list(dictionary.keys())
    inClassDist = 0
    incClassCount = 0
    outClassDist = 0
    outClassCount = 0
    for key in listkeys:
        for keys in listkeys:
            if (keys == key):
                elements = dictionary[keys]
                for element in elements:
                    for otherElements in elements:
                        if(otherElements != element):
                            inClassDist += model.similarity(otherElements, element)
                            incClassCount += 1
                if (len(elements) > 1):
                    distances["inclass"][key] = round(inClassDist/incClassCount,3)
                    inClassDist = 0
                    incClassCount = 0
            # else:
            #     for element in dictionary[key]:
            #         for otherElements in dictionary[keys]:
            #             outClassDist += model.similarity(otherElements, element)
            #             outClassCount += 1
            #         print(outClassCount)
            #         distances["betweenclass"][key + '-' + keys] = round(outClassDist/outClassCount,3)
            #         outClassDist = 0
            #         outClassCount = 0
    print(distances)
    return 0;




listToMeasureDistances = {"Energetics": ["HMX", "TATB", "RDX", "PETN", "TNT", "NTO"],\
                            "Binders": ["HTPB", "estane", "wax"],\
                            "Compositions": ["IMX-101", "IMX-104", "PBX-9501", "PBX-9502", "LX-17"],\
                            "Fuel": ["aluminum"]}

modelFilename = '2014DetSymp.bin'
model = KeyedVectors.load(modelFilename)

classDistances(model, listToMeasureDistances)
print("Done!")
