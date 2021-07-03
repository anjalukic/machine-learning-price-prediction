import json
import numpy as np

with open('preprocessedRealestate.json') as json_file:
    realestate = json.load(json_file)
    print(realestate)
    data = np.zeros((len(realestate), len(realestate[0].keys())))
    i = 0
    for r in realestate:
        j = 0
        for key in r:
            if r[key] is not None:
                data[i, j] = r[key]
            else:
                # if there's a NULL -> 0, warning - this will ruin the mean result!
                data[i, j] = 0
            j += 1
        i += 1

    normalizationData = []
    # normalize with mean value from each column, except for price column
    for col in range(data.shape[1]):
        if col == 0:
            continue
        colMax = np.max(data[:, col])
        colMin = np.min(data[:, col])
        if colMin != colMax:
            data[:, col] = (data[:, col] - colMin) / (colMax - colMin)
        else:
            data[:, col] = (data[:, col] - colMin) / colMax
        print('column max and min are ')
        print(colMax)
        print(colMin)
        normalizationData.append([colMin, colMax])
    # print(data)
    # now we have normalized data matrix with columns price, distance, squareFootage, numberOfRooms

    # print(data)
    # shuffle the data
    np.random.shuffle(data)

    with open('normalizedRealestate.json', 'w') as outfile:
        obj = data.tolist()
        json.dump(obj, outfile, indent=4)
        # print(np.array(obj))

    with open('normalizationData.json', 'w') as outfile:
        json.dump(normalizationData, outfile, indent=4)
