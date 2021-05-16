import re
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import time

os.chdir('/Users/caishuo/github/IBI1_2020-21/Practical14')
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
all_term = collection.getElementsByTagName("term")

name = locals()
#define a function that can get term contain specific string in its defstr.
def find_specificed_term(str):
    name[str+'_list'] = []
    for i in all_term:
        defstr = i.getElementsByTagName('defstr')[0].childNodes[0].data
        if re.search(str, defstr):
            term_id = i.getElementsByTagNameNS(i.namespaceURI, 'id')[0].childNodes[0].data
            name[str+'_list'].append(term_id)

#-*-I chose oligosaccharide as the forth macromolecule-*-
#get all term that contain 'DNA', 'RNA', 'protein', 'oligosaccharide' in defstr.
molecule_list = ['DNA', 'RNA', 'protein', 'oligosaccharide']
for molecule in molecule_list:
    find_specificed_term(molecule)

#==============================================================================#
#class every nodes to a Node object.
#Node object have three attributes: id, children, parent.
class Node:
    def __init__(self, id, children = [], parent = []):
        self.id = id
        self.children = children
        self.parent = parent

#Create Node object for every term element
name = locals()
Nodes = []
for term in all_term:
    term_id = term.getElementsByTagNameNS(term.namespaceURI, 'id')[0].childNodes[0].data
    is_a_list = []
    for id in term.getElementsByTagNameNS(term.namespaceURI, 'is_a'):
        is_a_list.append(id.childNodes[0].data)
    #Name the Node object by its id
    #Is_a tags describe the parent node id of the element under consideration
    #give id and parent value to Node object
    name[''+term_id] = Node(term_id, [], is_a_list)
    Nodes.append(name[''+term_id])

#give children list to Node object (in a way that can avoid traversing)
for Node in Nodes:
    for parent_id in Node.parent:
        name[''+parent_id].children.append(Node.id)

#The steps above build a 'node tree', in which we can assess childNodes of a node easily.

#Define a recursive function that find every descendant of a given Node
def find_descendant(Node):
    for child in Node.children:
        descendant.append(child)
        #if the child of one node still have children
        #Then the function will call itself to find the children of children,
        #the rest can be done in the same manner.
        find_descendant(name[''+child])
    return descendant

#count the number of all four macromolecule
count_list = []
#For every rootNode that contain molecule name
for molecule in molecule_list:
    time_start=time.time()
    descendant = []
#put all the desendants into a set
    AnsL = set()
    for element in name[molecule+'_list']:
        if not element in AnsL:
            #joint all the desendents of a single rootNode into the set
            AnsL = AnsL.union(find_descendant(name[''+element]))
    time_end=time.time()
    #Output name and childNodes number
    print('the number of childNodes associated with '+molecule+' is '+str(len(AnsL)))
    print('time cost is %.2fs'%(time_end-time_start))
    name[molecule+'_count'] = len(AnsL)
    count_list.append(name[molecule+'_count'])

#==============================================================================#

#Draw a pie chart describing the of childNodes of DNA, RNA, protein and oligosaccharide.
import matplotlib.pyplot as plt
#give attribute to the plot.
labels = []
#generate labels cotain name and count of four molecules for the pie chart.
for molecule in molecule_list:
    label = molecule+':'+str(name[molecule+'_count'])
    labels.append(label)

labels = tuple(labels)
sizes = count_list
explode = (0.01,0.01,0.005,0.15)
colors = ['#90EE90', '#87CEFA', '#F5DEB3', '#FFB6C1']

fig1, ax1 = plt.subplots(figsize=(8, 4))
# ax1.axis('equal')
ax1.pie(sizes,explode = explode, labels = labels, autopct = '%1.1f%%', shadow = False,
        startangle = 150, colors=colors)

ax1.legend(molecule_list,
          title="molecule",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

ax1.set_title('ChildNodes of four biological macromolecules')
plt.show()
