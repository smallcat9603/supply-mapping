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
# 情報入力
#######################

#工場数
num_location = 4
#製品数
num_product = 6

#製品-工場のマッピング、0は工場A、1は工場B、...
supply_mapping = [0] * num_product
#コスト最適化後の結果
location_bestfit = {}

#製品間の依存関係
product_parts = {
    6:[3, 4, 5],
    3:[1, 2]
}

#時間コスト
time_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]
}

#コスト
dollar_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]    
}

#製品の工場効率
efficiency = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]    
}

#工場間の物理距離
physical_distance = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]
]

#製品間の調整関係
adjust_relation = [
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
]

#工場間の社会関係
social_relation = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]    
]

#工場の生産能力
location_capability = [1, 2, 3, 4]

#製品の需要個数
product_demand = [1, 2, 3, 4] 


def main():
    for factory in range(num_location):
        supply_mapping[num_product-1] = factory
        cost_min = 0
        cost_production_min = 0
        cost_transportation_min = 0
        cost_adjust_min = 0
        for product in range(num_product-1):
            for location in range(num_location):
                supply_mapping[product] = location
                cost_production = cal_cost_production(product, location)
                cost_transportation = cal_cost_transportation(product, location)
                cost_adjust = cal_cost_adjust(product, location)
                cost = cost_production + cost_transportation + cost_adjust
                if cost > cost_min:
                    cost_min = cost
                    cost_production_min = cost_production
                    cost_transportation_min = cost_transportation
                    cost_adjust_min = cost_adjust
    print_result()

def cal_cost_production(product, location):
    return time_cost[product+1][location] * dollar_cost[product+1][location] * efficiency[product+1][location]

def cal_cost_transportation(product, location):
    

def cal_cost_adjust(product, location):


def print_result():


if __name__ == "__main__":
   main()      