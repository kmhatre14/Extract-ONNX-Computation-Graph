##################################################
# Extracting Computational Graph form a onnx file
# Author : Kaustubh (^_^)
# University of North Carolina Charlotte
# Date : 09/15/2019
##################################################

import onnx as ox
import matplotlib.pyplot as plt
import argparse
import networkx as nx

#Create Networkx Ggaph from nodes
def createNWxGraph(allnode,nwxg):
    for node in allnode:
        print(node.op_type,node.input,node.output)
        nwxg.add_node(node.output[0])
    for node in allnode:
        for everyNode in allnode:
            if node.output[0] in everyNode.input:
                for i in range(len(everyNode.input)):
                    if node.output[0] == everyNode.input[i]:
                        nwxg.add_edge(everyNode.output[0],node.output[0])
#                        print("added Edge")
#                        print(node.output[0],"is",everyNode.output[0])
#        nwxg.add_edge(node.input[0],node.output[0]) 
#        if node.op_type == 'Add':
#            nwxg.add_edge(node.input[1],node.output[0])
    return nwxg


#Extract the weights from the model
def extractWeights(mg):
    allWeights = [n for n in mg.initializer]
    print("Number of Wights Matrix in Model : "+str(len(allWeights)))    
    for w in allWeights:
        print(w.name)    

#Extract the full graph from the model
def extractGraph(mg):
    allNodes = [n for n in mg.node]
    print("Number of Nodes in Graph : "+str(len(allNodes)))
    print("Layer \t Input \t output")
    return allNodes
#    for node in allNodes:
#        print(node.op_type,node.input,node.output)
#        if node.op_type == 'Add':
#            print("Input Node:"+str(node.input))
#            print("Out Node:"+str(node.output))
    #print(allNodes[0])

#main  
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()  
    # Load Model
    model = ox.load(args.file)
    #create a NWx graph 
    NWg = nx.Graph()
    modelGraph = model.graph
    NWg = createNWxGraph(extractGraph(modelGraph),NWg)
    nx.draw_networkx(NWg,with_labels=True)
    plt.show()
    #extractGraph(modelGraph)
    #extractWeights(modelGraph)

# Define main function
if __name__ == '__main__': 
    main()
