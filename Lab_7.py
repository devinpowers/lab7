#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:09:54 2020

@author: devinpowers
"""

import csv

from operator import itemgetter


INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Read file, skip first 3 headers and return list of lists, skipping empty rows in csv file'''
    
    L = []
    reader = csv.reader(fp)
    next(reader,None)
    next(reader,None)
    next(reader,None)
    next(reader,None)
    
    for line in reader:
        if not line:
            continue  #skip empty lines
        else:
            L.append(line)        
    return L

def get_totals(L):
    ''' Get US total from US at index 1, and then get sum of index for the States and return both numbers'''
   
    # USA pop is in index shown and then we strip the comma 
    
    us_pop = int(L[0][1].replace(',',''))

    new_list =[]   #new list, which will include only number of unauthorized immigrant population
    
    # for each element in index 1 of each list I replaced the comma and the < sign if needed and appended to a new list
    for element in L[1:]:
        new_list.append(int(element[1].replace(',','').replace('<','')))        
    
    #summed new list here 
    
    total_pop = sum(new_list)       

    return us_pop, total_pop


def get_largest_states(L):
    
    ''' Return a list of  states that have higher % than then us average '''
    
    us_pop_average = float(L[0][2].replace('%',''))
    
    states = []
    
    for element in L[1:]:
        if float(element[2].replace('%','')) > us_pop_average:
            states.append(element[0])    
   
    
    return states
    


def get_industry_counts(L):
    '''Counted the Industries '''
    
    Agriculture = 0
    Business_services = 0
    Construction = 0
    Leisure = 0
    Manufacturing = 0
    
    industry_count = []
    
    for element in L[1:]:
        if element[9] == 'Agriculture':
            Agriculture += 1
        elif element[9] == 'Business services':
            Business_services  += 1
        elif element[9] == 'Leisure/hospitality':
            Leisure += 1
        elif element[9] == 'Manufacturing':
            Manufacturing += 1
        elif element[9] == 'Construction':
             Construction += 1
        else:
            continue
    
    industry_count = [['Agriculture',Agriculture],['Business services',Business_services], ['Construction',Construction],['Leisure/hospitality',Leisure],['Manufacturing',Manufacturing]]
    
    industry_sorted = sorted(industry_count, key=itemgetter(1), reverse= True)
        
        
    return industry_sorted  # temoprary return value so main runs
    


def main():    
    fp = open("immigration.csv")
    
    # returns list of lists
    L = read_file(fp)
   
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()