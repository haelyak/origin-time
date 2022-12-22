from hiv1Mgroup import *

exTree=('anc', ('anc', (2007, (), (), 7.0), (1993, (), (), 3.0), 2.0), (1999, (), (), 7.0), 0)

exTree2=('anc',('anc',('anc',(2010,(),(),.01),(2007,(),(),.015),.02),(1994,(),(),.01),.01),('anc',('anc',(2001,(),(),.01),('anc',(2006,(),(),.02),(2004,(),(),.015),.01),.01),(2006,(),(),.03),.03),0)

def writeData(tree,fileName):
    '''Call extractData to get collection times and branch lengths, then
write these to file in tab-delimited form.'''
    L=extractData(tree)
    f=open(fileName,"w")
    for ct,br in L:
        f.write(str(ct)+"\t"+str(br)+"\n")
    f.close()

def extractData(tree):
    '''Returns a list of lists, each of which contains a leaf date, with the cumulative branch length to get to that leaf'''
    if tree[0] == 'anc':
        rightLength = tree[1][3]
        leftLength = tree[2][3]
        rightTree = extractData(tree[1])
        leftTree = extractData(tree[2])
        for leaf in rightTree:
            leaf[1] += rightLength
        for leaf in leftTree:
            leaf[1] += leftLength
        return rightTree + leftTree
    else:
        return [[tree[0], 0]]

