#@Brief : python script that collects the data from the benchmarks and plots them
#@Author :Dimitris Vlachos (csd4492)
#@hy425 Programming Assignment #1


import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import pandas as pd

class Benchmark:
 
 def __init__(self,Bench_name):
    self.Bench_name = Bench_name
    self.predictors = []
 def add_predictor(self,predictor):
    self.predictors.append(predictor)
    
 def get_name(self):
    print(self.Bench_name)

 def pred_data(self):
    self.predictor.get_data() 

 def get_pred(self):
    return self.predictors

class Predictor:
   
    def __init__(self, name,data,type):
        self.name = name
        self.data = data
        self.type = type
    def myfunc(self):
        print(self.name)
    def get_data(self):
        return self.data
       



def get_data_again(file):
    with open(file, "r") as text_file:
        data= [int(line.split("\n")[0]) for line in text_file]
    return data


def get_benchmarks():
    cc = 0
    benchmarks = []
    benchmark_files ={"benchmark1/","benchmark2/","benchmark3/","benchmark4/","benchmark5/"}
    for path in sorted(benchmark_files):
        
        b1 = Benchmark(path.replace('/',' '))
        for file in sorted(os.listdir(path)):
            
            if file.endswith(".txt"):
                if "GAp" in file:
                    b1.add_predictor(Predictor(file,get_data_again(path+file),"GAp"))
                elif "PAg" in file:
                    b1.add_predictor(Predictor(file,get_data_again(path+file),"PAg"))
                elif "Static" in file:
                    b1.add_predictor(Predictor(file,get_data_again(path+file),"Static"))
                elif "Local" in file:
                    b1.add_predictor(Predictor(file,get_data_again(path+file),"Local"))           

        benchmarks.insert(cc,b1)
        cc+=1
       
        
    return benchmarks            



def percent(part, whole):
    return 100 * float(part)/float(whole)




benchmarks = get_benchmarks()
for b in benchmarks:
    print("BENCHMARK:",b.Bench_name,"\n")
    for p in b.predictors:
        print("name",p.name,"data",p.data)


def plot_2048():

    barWidth = 0.1
    fig = plt.subplots(figsize =(12, 8))
    GAP = []
    PAG =[]
    ST = []
    LC = []


    for b in benchmarks:
      
        GAP .append(b.predictors[1].data[1])
        PAG.append( b.predictors[5].data[1])
        LC.append(b.predictors[3].data[1])
        ST.append(b.predictors[7].data[1])
 

    br1 = np.arange(len(GAP))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    print (GAP)

    plt.bar(br1, GAP, color ='r', width = barWidth,
        edgecolor ='grey', label ="GAp")
    plt.bar(br2, PAG, color ='g', width = barWidth,
        edgecolor ='grey', label ="PAg")
    plt.bar(br3, ST, color ='b', width = barWidth,
        edgecolor ='grey', label ="Static")
    plt.bar(br4, LC, color ='y', width = barWidth,
        edgecolor ='grey', label ="Local")

    plt.xlabel('Benchmark#', fontweight ='bold', fontsize = 15)
    plt.ylabel('Mispredictions', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(GAP))],
        ['Benchmark1', 'Benchmark2', 'Benchmark3', 'Benchmark4', 'Benchmark5'])

    plt.legend()
    plt.show()

    pag_per=[]
    gap_per =[]
    static_per = []    
    local_per = []
    for b in benchmarks:
        gap_per.append(percent(b.predictors[1].data[1],b.predictors[1].data[0]))
        pag_per.append(percent(b.predictors[5].data[1],b.predictors[5].data[0]))
        local_per.append(percent(b.predictors[3].data[1],b.predictors[3].data[0]))
        static_per.append(percent(b.predictors[7].data[1],b.predictors[7].data[0]))

    df = pd.DataFrame({'GAp': gap_per,'PAg': pag_per,'Static ':static_per ,'Local ':local_per})
    ax = df.plot.barh()
    ax.axhline(0, color='grey', linewidth=0.8)
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    ax.bar_label(ax.containers[2])
    ax.bar_label(ax.containers[3])
    plt.show()



barWidth = 0.1
fig = plt.subplots(figsize =(12, 8))
GAP = []
PAG =[]
ST = []
LC = []


for b in benchmarks:
      
    GAP .append(b.predictors[0].data[1])
    PAG.append( b.predictors[4].data[1])
    LC.append(b.predictors[2].data[1])
    ST.append(b.predictors[6].data[1])
 

br1 = np.arange(len(GAP))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]
print (GAP)

plt.bar(br1, GAP, color ='r', width = barWidth,
        edgecolor ='grey', label ="GAp")
plt.bar(br2, PAG, color ='g', width = barWidth,
        edgecolor ='grey', label ="PAg")
plt.bar(br3, ST, color ='b', width = barWidth,
        edgecolor ='grey', label ="Static")
plt.bar(br4, LC, color ='y', width = barWidth,
        edgecolor ='grey', label ="Local")

plt.xlabel('Benchmark#', fontweight ='bold', fontsize = 15)
plt.ylabel('Mispredictions', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(GAP))],
        ['Benchmark1', 'Benchmark2', 'Benchmark3', 'Benchmark4', 'Benchmark5'])

plt.legend()
plt.show()


pag_per=[]
gap_per =[]
static_per = []    
local_per = []
for b in benchmarks:
    gap_per.append(percent(b.predictors[0].data[1],b.predictors[0].data[0]))
    pag_per.append(percent(b.predictors[4].data[1],b.predictors[4].data[0]))
    local_per.append(percent(b.predictors[2].data[1],b.predictors[2].data[0]))
    static_per.append(percent(b.predictors[6].data[1],b.predictors[6].data[0]))

df = pd.DataFrame({'GAp': gap_per,'PAg': pag_per,'Static ':static_per ,'Local ':local_per})
ax = df.plot.barh()
ax.axhline(0, color='grey', linewidth=0.8)
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
ax.bar_label(ax.containers[2])
ax.bar_label(ax.containers[3])
plt.show()

print("Now plotting for 2048  memory budget\n")
plot_2048()