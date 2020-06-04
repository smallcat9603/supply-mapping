'''
Created on 2020/06/04
This program provides a solution of factory-goods mapping.
@author: hq
'''

import datetime
import networkx as nx   
import sys, getopt
import pandas as pd

#number of plants
num_location = 4
#number of products
num_product = 6

#product-plant mapping
supply_mapping = [0] * num_product

#product relation
product_parts = {
    6:[3, 4, 5],
    3:[1, 2]
}

#time cost
time_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]
}

#dollar cost
dollar_cost = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]    
}

#product efficiency
efficiency = {
    1:[1, 2, 3, 4],
    2:[1, 2, 3, 4],
    3:[1, 2, 3, 4],
    4:[1, 2, 3, 4],
    5:[1, 2, 3, 4],
    6:[1, 2, 3, 4]       
}

#plant distance
physical_distance = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]
]

#adjust relation of products
adjust_relation = [
    [1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

#social relation of plants
social_relation = [
    [0, 1, 2, 3],
    [1, 0, 3, 4],
    [2, 3, 0, 5],
    [3, 4, 5, 0]    
]

#adjust capability of plants
location_capability = [1, 2, 3, 4]

#demands
product_demand = [1, 2, 3, 4] 


def main():
    print "Number of plants: ", num_location
    print "Number of products: ", num_product
    print "Optimization result: " 
    for factory in range(num_location):
        if product_demand[factory] > 0:
            supply_mapping[num_product-1] = factory
            cost_min = 10000
            cost_production_min = 0
            cost_transportation_min = 0
            cost_adjust_min = 0
            cost_min_2 = 10000
            cost_production_min_2 = 0
            cost_transportation_min_2 = 0
            cost_adjust_min_2 = 0            
            # for b in range(pow(2, num_product-1)):        
            #     for product in range(num_product-1):
            #         supply_mapping[product] = (bin(b)>>product)&1
            for p0 in range(num_location):
                for p1 in range(num_location):
                    for p2 in range(num_location):
                        for p3 in range(num_location):
                            for p4 in range(num_location):
                                supply_mapping[0] = p0
                                supply_mapping[1] = p1
                                supply_mapping[2] = p2
                                supply_mapping[3] = p3
                                supply_mapping[4] = p4
                                cost_production = cal_cost_production()
                                cost_transportation = cal_cost_transportation()
                                cost_adjust = cal_cost_adjust()
                                cost = cost_production + cost_transportation + cost_adjust
                                cost_2 = cost_production + cost_transportation
                                if cost < cost_min:
                                    cost_min = cost
                                    cost_production_min = cost_production
                                    cost_transportation_min = cost_transportation
                                    cost_adjust_min = cost_adjust  
                                if cost_2 < cost_min_2:
                                    cost_min_2 = cost_2
                                    cost_production_min_2 = cost_production
                                    cost_transportation_min_2 = cost_transportation
                                    cost_adjust_min_2 = cost_adjust
            print_result(factory, cost_min, cost_production_min, cost_transportation_min, cost_adjust_min)
            print_mapping()
            print_result_2(factory, cost_min_2, cost_production_min_2, cost_transportation_min_2, cost_adjust_min_2)
            print_mapping()

def cal_cost_production():
    cost_production = 0
    for product in range(num_product):
        location = supply_mapping[product]
        cost_production = cost_production + time_cost[product+1][location] * dollar_cost[product+1][location] * efficiency[product+1][location]
    return cost_production

def cal_cost_transportation():
    cost_transportation = 0
    for key in product_parts:
        for value in product_parts[key]:
            location_key = supply_mapping[key-1]
            location_value = supply_mapping[value-1]
            cost_transportation = cost_transportation + physical_distance[location_key][location_value]
    return cost_transportation

def cal_cost_adjust():
    cost_adjust = 0
    for p in range(num_product):
        for pp in range(p, num_product):
            if adjust_relation[p][pp] == 1:
                location_p = supply_mapping[p]
                location_pp = supply_mapping[pp]
                cost_adjust = cost_adjust + pow(social_relation[location_p][location_pp], 2)/(location_capability[location_p]*location_capability[location_pp])
    return cost_adjust

def print_result(factory, cost_min, cost_production_min, cost_transportation_min, cost_adjust_min):
    print "Plant", factory, ": "
    print "Total cost (3 considered): ", cost_min, " (production cost: ", cost_production_min, ", transportation cost: ", cost_transportation_min, ", adjust cost: ", cost_adjust_min, ")"

def print_result_2(factory, cost_min_2, cost_production_min_2, cost_transportation_min_2, cost_adjust_min_2):
    print "Plant", factory, ": "
    print "Total cost (2 considered): ", cost_min_2, " (production cost: ", cost_production_min_2, ", transportation cost: ", cost_transportation_min_2, ", adjust cost: ", cost_adjust_min_2, ")"

def print_mapping():
    print "product --> plant:"
    for product in range(num_product):
        print product+1, " --> ", supply_mapping[product]

if __name__ == "__main__":
   main()      