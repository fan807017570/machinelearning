import pandas as pd
import numpy as np
from sklearn import datasets
from math import log
import logging
import sys

logger = logging.getLogger("CartTree")
# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


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


# compute the dividing points for continuous property
def calBinaryForContinousProperty(target, dataset, propIndex):
    entropy = CalcEntropy(target)
    colomn = dataset[:, propIndex]
    colomn_list = []
    for i in range(len(colomn)):
        tuple_label = [colomn[i], target[i]]
        colomn_list.append(tuple_label)
    length = len(colomn_list)
    last_entropy = 0
    index = 0
    sorted_list = sorted(colomn_list)
    logger.info("sorted list:%s", sorted_list)
    for j in range(len(colomn_list)):
        if j != 0 and j != length - 1:
            colomn_left = np.array(sorted(colomn_list)[:j])
            left_target = colomn_left[:, 1]
            left_entropy = j / length * CalcEntropy(left_target)
            logger.debug("left_target:%s", left_entropy)
            colomn_right = np.array(sorted(colomn_list)[j + 1:])
            right_target = colomn_right[:, 1]
            right_entropy = (length - j) / length * CalcEntropy(right_target)
            tmp = entropy - left_entropy - right_entropy
            if tmp > last_entropy:
                last_entropy = tmp
                index = j
            logger.debug("right_target:%s", right_entropy)
    print("index is :{},and the item is {}".format(index, sorted_list[index]))
    f = sorted_list[index]
    s = sorted_list[index + 1]
    print(type(f))
    return (f[0] + s[0]) / 2


def calGain(target, dataset, propIndex):
    logger.info("starting compute the gain for Decided tree!")
    entropy = CalcEntropy(target)
    divided_point = calBinaryForContinousProperty(target, dataset, propIndex)
    all_data = np.c_[dataset, target]
    shape = all_data.shape;
    sorted_data = all_data[all_data[:0].argsort()]
    left_set = []
    right_set = []
    for index in range(len(all_data)):
        item = all_data[index + 1:propIndex + 1]
        if item < divided_point:
            left_set.append(all_data[index])
        elif item > divided_point:
            right_set.append(all_data[index])
    print(type(shape[1]))
    print(type(shape[0]))
    col = shape[1] - 1
    print(left_set)
    # left_target = np.array(left_set)[:, 3]
    # right_target = np.array(right_set)[:, 3]
    # gain = entropy - (len(left_set) * CalcEntropy(left_target) + len(right_set) * CalcEntropy(right_target)) / len(
    #     all_data)
    # return gain


data, target = loadData()
gain = calGain(target, data, 0)
print(gain)
# divided_point = calBinaryForContinousProperty(target, data, 3)
# print(divided_point)
# print(type(data))
# dataset = np.c_[data, target]
# print(dataset[dataset[:, 0].argsort()])  # sort the array by colomn 0










# print(data)
# colomn = data[:, 0]
# # print(colomn)
# colomn_list = []
# for i in range(len(colomn)):
#     tuple_label = [colomn[i], target[i]]
#     colomn_list.append(tuple_label)
# print("colomn_list:{}".format(colomn_list))
# # print(np.array(colomn_list))
# # print(sorted(colomn_list)[1:])
# length = len(colomn_list)
# last_entropy = 0
# index = 0
# sorted_list = sorted(colomn_list)
# print("sorted list:{}".format(sorted_list))
# for j in range(len(colomn_list)):
#     if j != 0 and j != length - 1:
#         colomn_left = np.array(sorted(colomn_list)[:j])
#         left_target = colomn_left[:, 1]
#         left_entropy = j / length * CalcEntropy(left_target)
#         print("left_target:{}".format(left_entropy))
#         # print("colomn_left:{}".format(colomn_left))
#         colomn_right = np.array(sorted(colomn_list)[j + 1:])
#         right_target = colomn_right[:, 1]
#         right_entropy = (length - j) / length * CalcEntropy(right_target)
#         tmp = entropy - left_entropy - right_entropy
#         if tmp > last_entropy:
#             last_entropy = tmp
#             index = j
#         print("right_target:{}".format(right_entropy))
# print("index is :{},and the item is {}".format(index, sorted_list[index]))

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
