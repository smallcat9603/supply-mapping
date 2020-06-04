'''
Created on 2020/06/04
This program provides a solution of factory-goods mapping.
@author: hq
'''

import datetime
import networkx as nx   
import sys, getopt
import pandas as pd

#######################
# input data
#######################

num_location = 4
num_product = 6

product_parts = {
    6:[3, 4, 5],
    3:[1, 2]
}

time_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]
}

dollar_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]    
}

efficiency = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]    
}

physical_distance = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]
]

adjust_relation = [
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

social_relation = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]    
]

location_capability = [1, 2, 3, 4]

product_demand = [1, 2, 3, 4] 


def main():
    for location in range(num_location):
        

    cost_production = 
    cost_transportation =
    cost_adjust =

if __name__ == "__main__":
   main()      