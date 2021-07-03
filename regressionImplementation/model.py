import json
import numpy as np
import matplotlib.pyplot as plt

hyperparameters = {'alpha': [0.01, 0.1], 'lambda': 0.01, 'miniBatchSize': [32, 64, 128], 'iterations': 20, 'k': 10}


def plotIt(list):
    x = range(0, len(list))
    plt.xlabel("Iteration")
    plt.ylabel("Loss function")
    plt.title("Loss function over time")
    for i in range(len(list[0])):
        plt.plot(x, [pt[i] for pt in list], label='id %s' % i)
    plt.legend()
    plt.show()
    return


def train(data, parameters, hyperparams, devSet, useDev, shouldPlot):
    costs = []
    avgCosts = []
    # return cost is going to be either the dev cost (if useDev == True) or RMSE
    returnCosts = []
    params = np.copy(parameters)
    batchSize = hyperparams['miniBatchSize']
    nOfIterations = hyperparams['iterations']
    for n in range(nOfIterations):
        costs = []
        returnCosts = []
        for i in range(0, data.shape[0], batchSize):
            miniBatch = np.copy(data[i:i + batchSize])
            # data has the price as the first column
            expectedOutput = np.copy(miniBatch[:, 0])
            miniBatch[:, 0] = 1

            # calculate the loss and cost function
            hypothesis = np.transpose(np.matmul(params, np.transpose(miniBatch)))
            loss = hypothesis - expectedOutput
            costFunction = np.sum(np.square(loss)) / (2 * miniBatch.shape[0])
            costs.append(costFunction)

            # prepare the dev set and calculate hypothesis (1xSizeOfDevSet)
            if useDev:
                devBatch = np.copy(devSet)
                devExpectedOutput = np.copy(devSet[:, 0])
                devBatch[:, 0] = 1
                devHypothesis = np.transpose(np.matmul(params, np.transpose(devBatch)))
                devLoss = devHypothesis - devExpectedOutput
                devCostFunction = np.sum(np.square(devLoss)) / (2 * devBatch.shape[0])
                returnCosts.append(devCostFunction)
            else:
                rmse = np.sqrt(np.sum(np.square(loss)) / miniBatch.shape[0])
                returnCosts.append(rmse)

            # update the parameters
            deltaParams = np.matmul(np.transpose(loss), miniBatch)
            params = params - (hyperparams['alpha'] / miniBatch.shape[0]) * deltaParams
            ''' or - with regularization
            param0 = params[0]
            params = params - (hyperparams['alpha'] / miniBatch.shape[0]) * (deltaParams+hyperparams['lambda']*params)
            params[0] = params[0] + (hyperparams['alpha']*hyperparams['lambda'] / miniBatch.shape[0])*param0
            '''

        avgCosts.append([np.mean(costs), np.mean(returnCosts)])
        # print('average cost is '+str(np.mean(costs)))
    if shouldPlot:
        plotIt(avgCosts)
    return params, returnCosts[len(returnCosts) - 1]


with open('normalizedRealestate.json') as json_file:
    dataList = json.load(json_file)
    data = np.array(dataList)
    # data contains columns price, distance, squareFootage and numberOfRooms
    # print(data)

    outerFolds = np.array_split(data, hyperparameters['k'])
    hypersOuterVotes = np.zeros(len(hyperparameters['alpha']) * len(hyperparameters['miniBatchSize']))
    costsForHypersOuter = []

    # outer cross validation for evaluation
    for outerInd, testData in enumerate(outerFolds):
        print('Outer loop: ' + str(outerInd+1))
        # print(testSet)

        # make the training and dev set from the rest of the outer folds
        trainDevSet = np.concatenate([fold for i, fold in enumerate(outerFolds) if i != outerInd])

        parameters = np.zeros(np.shape(trainDevSet)[1])

        # split the training and dev set to folds
        innerFolds = np.array_split(trainDevSet, hyperparameters['k'])

        costsForHypersInner = np.zeros((hyperparameters['k'], len(hyperparameters['alpha']) * len(hyperparameters['miniBatchSize'])))

        # inner cross validation for validation and hyperparameters selection
        for innerInd, devSet in enumerate(innerFolds):

            # make the training set from the rest of the inner folds
            trainingSet = np.concatenate([fold for i, fold in enumerate(innerFolds) if i != innerInd])

            print('.', end=" ")

            # try every combination of hyperparameters
            for alphaInd, alpha in enumerate(hyperparameters['alpha']):
                for miniBatchInd, miniBatchSize in enumerate(hyperparameters['miniBatchSize']):
                    currentHyperparams = {'alpha': alpha, 'lambda': hyperparameters['lambda'], 'miniBatchSize': miniBatchSize, 'iterations': hyperparameters['iterations']}
                    temp, cost = train(trainingSet, parameters, currentHyperparams, devSet, useDev=True, shouldPlot=False)
                    costsForHypersInner[innerInd, alphaInd * len(hyperparameters['miniBatchSize']) + miniBatchInd] = cost

        print('')
        avgCostsHypersInner = list(np.array(costsForHypersInner).mean(axis=0))
        bestHypersComboInd = avgCostsHypersInner.index(min(avgCostsHypersInner))
        print('best hypers for the outer loop '+str(outerInd)+' are: ')
        print('alpha = ' + str(hyperparameters['alpha'][bestHypersComboInd // len(hyperparameters['miniBatchSize'])]))
        print('miniBatchSize = ' + str(hyperparameters['miniBatchSize'][bestHypersComboInd % len(hyperparameters['miniBatchSize'])]))
        hypersOuterVotes[bestHypersComboInd] = hypersOuterVotes[bestHypersComboInd] + 1
        costsForHypersOuter.append(avgCostsHypersInner)

    # print(hypersOuterVotes)
    avgCostsOuter = list(np.array(costsForHypersOuter).mean(axis=0))
    # print(avgCostsOuter)
    bestHypersCombo = avgCostsOuter.index(min(avgCostsOuter))
    alpha = hyperparameters['alpha'][bestHypersCombo // len(hyperparameters['miniBatchSize'])]
    miniBatchSize = hyperparameters['miniBatchSize'][bestHypersCombo % len(hyperparameters['miniBatchSize'])]
    print('Best hypers for the model are: ')
    print('alpha = ' + str(alpha))
    print('miniBatchSize = ' + str(miniBatchSize))


    alpha = 0.1
    miniBatchSize = 32

    # outer cross validation again for performance evaluation
    print("Training and evaluating the model:")
    evalMAE = []
    evalRAE = []
    hyperparams = {'alpha': alpha, 'lambda': hyperparameters['lambda'], 'miniBatchSize': miniBatchSize, 'iterations': hyperparameters['iterations']}
    for outerInd, testData in enumerate(outerFolds):
        print('.', end=" ")

        # make the training from the rest of the outer folds
        trainSet = np.concatenate([fold for i, fold in enumerate(outerFolds) if i != outerInd])

        parameters = np.zeros(np.shape(trainSet)[1])
        parameters, cost = train(trainSet, parameters, hyperparams, None, useDev=False, shouldPlot=False)

        testExpectedOutput = np.copy(testData[:, 0])
        testSet = np.copy(testData)
        testSet[:, 0] = 1
        hypothesis = np.transpose(np.matmul(parameters, np.transpose(testSet)))
        loss = testExpectedOutput - hypothesis

        # absolute error
        mae = np.sum(np.absolute(loss)) / loss.shape[0]
        evalMAE.append(mae)

        # relative errors
        meanExpectedOutput = np.mean(testExpectedOutput)
        rae = np.sum(np.absolute(loss)) / np.sum(np.absolute(loss - meanExpectedOutput))
        evalRAE.append(rae)

    print('')
    print('Average MAE is ' + str(round(np.mean(evalMAE), 2)) + ' euros')
    print('Average RAE is ' + str(round(np.mean(evalRAE), 2)))

    # train the model on all data
    parameters = np.zeros(np.shape(trainSet)[1])
    parameters, _ = train(data, parameters, hyperparams, None, useDev=False, shouldPlot=False)

    with open('modelParameters.json', 'w') as outfile:
        obj = parameters.tolist()
        json.dump(obj, outfile, indent=4)







