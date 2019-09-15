##################################################
# Extracting Computational Graph form a onnx file
# Author : Kaustubh (^_^)
# University of North Carolina Charlotte
# Date : 09/15/2019
##################################################

import onnx as ox
import matplotlib.pyplot as plt


#Extract the full graph from te 
def extractGraph(mg):
    allNodes = [n for n in mg.node]
    print("Number of Nodes in Graph : "+str(len(allNodes)))
    print("Layer \t Input \t output")
    for node in allNodes:
        print(node.op_type,node.input,node.output)
#        if node.op_type == 'Add':
#            print("Input Node:"+str(node.input))
#            print("Out Node:"+str(node.output))
    #print(allNodes[0])

#main  
def main():
    # Load Model
    model = ox.load('mobileNet.onnx')
    modelGraph = model.graph
    extractGraph(modelGraph)

# Define main function
if __name__ == '__main__': 
    main()
