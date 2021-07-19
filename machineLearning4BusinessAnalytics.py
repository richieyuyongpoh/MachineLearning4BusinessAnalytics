
import dill

activateFile = 'initMachineLearning4BusinessAnalyticsModule.pkl'
infile = open(activateFile,'rb')

initMachineLearning4BusinessAnalyticsAIHelper = dill.load(infile)
infile.close()


initMachineLearning4BusinessAnalyticsAIHelper()