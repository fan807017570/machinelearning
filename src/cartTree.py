import pandas as pd
import numpy as np
from sklearn import datasets
from math import log


class CartTree():
    def __init__(self, dataSet, target):
        self.dataSet = dataSet
        self.target = target

    def CalGain(self):
        print("hello ")
        0

    def CalcEntropy(self):
        label_count = {}
        label_percent = {}
        total = len(self.target)
        for i in self.target:
            if i not in label_count.keys():
                label_count[i] = 1
            else:
                if i == 1:
                    label_count[i] += 1
                else:
                    label_count[i] += 1
        entropy = 0
        for key in label_count.keys():
            label_percent[key] = label_count[key] / total
            prob = label_percent[key]
            entropy -= prob * log(prob, 2)
        return entropy

    def createTree(self):
        print("create tree")

    def testHoursing(self):
        print("test hoursing")


def loadData():
    iris_data = datasets.load_iris()
    data = iris_data.data
    target = iris_data.target
    return data, target


def CalcEntropy(target):
    label_count = {}
    label_percent = {}
    total = len(target)
    for i in target:
        if i not in label_count.keys():
            label_count[i] = 1
        else:
            if i == 1:
                label_count[i] += 1
            else:
                label_count[i] += 1
    entropy = 0
    for key in label_count.keys():
        label_percent[key] = label_count[key] / total
        prob = label_percent[key]
        entropy -= prob * log(prob, 2)
    return entropy


#
def calGain(target, dataset):
    print("caculate the gain")


data, target = loadData()
print(target)
entropy = CalcEntropy(target)
print()
# print(data)
colomn = data[:, 1]
# print(colomn)
colomn_list = []
for i in range(len(colomn)):
    tuple_label = [colomn[i], target[i]]
    colomn_list.append(tuple_label)
print("colomn_list:{}".format(colomn_list))
# print(np.array(colomn_list))
# print(sorted(colomn_list)[1:])
length = len(colomn_list)
last_entropy = 0
index = 0
sorted_list = sorted(colomn_list)
print("sorted list:{}".format(sorted_list))
for j in range(len(colomn_list)):
    if j != 0 and j != length - 1:
        colomn_left = np.array(sorted(colomn_list)[:j])
        left_target = colomn_left[:, 1]
        left_entropy = j / length * CalcEntropy(left_target)
        print("left_target:{}".format(left_entropy))
        # print("colomn_left:{}".format(colomn_left))
        colomn_right = np.array(sorted(colomn_list)[j + 1:])
        right_target = colomn_right[:, 1]
        right_entropy = (length - j) / length * CalcEntropy(right_target)
        tmp = entropy - left_entropy - right_entropy
        if tmp > last_entropy:
            last_entropy = tmp
            index = j
        print("right_target:{}".format(right_entropy))
print("index is :{},and the item is {}".format(index,sorted_list[index]))

# print("colomn_right:{}".format(right_target))
# colomn_targets = sorted(colomn_list)[:]
# print(colomn_targets)
# colomn_array = np.array(colomn_targets)
# print(colomn_array[4:, 1])
# print(colomn_targets)
# print(colomn_targets[1:10][1:2])
# print(colomn_targets[:, 1])
# print(colomn_targets)
# print(sorted(data[:,3]))
# t = CartTree()
# t.testHoursing()
# t.loadData()
