class univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnNames in dataset.columns:
            if(dataset[columnNames].dtype=='O'):
                qual.append(columnNames)
            else:
                quan.append(columnNames)
        return quan,qual
    
    def freqTable(columnname,dataset):
        FreqTable=pd.DataFrame(columns=["Unique_value","Frequency","Relative_frequency","Cumsum"])
        FreqTable["Unique_value"]=dataset[columnname].value_counts().index
        FreqTable["Frequency"]=dataset[columnname].value_counts().values
        FreqTable["Relative_frequency"]=(FreqTable["Frequency"]/len(FreqTable.index))
        FreqTable["Cumsum"]=FreqTable["Relative_frequency"].cumsum()
        return FreqTable
    
    def univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1=25%","Q2=50%","Q3=75%","99%","Q4=100%","IQR","1.5rule","Lowest","Greatest","Min","Max"],columns=quan)
        for columnname in descriptive.columns:
            descriptive[columnname]["Mean"]=dataset[columnname].mean()
            descriptive[columnname]["Median"]=dataset[columnname].median()
            descriptive[columnname]["Mode"]=dataset[columnname].mode()[0]
            descriptive[columnname]["Q1=25%"]=dataset.describe()[columnname]["25%"]
            descriptive[columnname]["Q2=50%"]=dataset.describe()[columnname]["50%"]
            descriptive[columnname]["Q3=75%"]=dataset.describe()[columnname]["75%"]
            descriptive[columnname]["99%"]=np.percentile(dataset[columnname],99)
            descriptive[columnname]["Q4=100%"]=dataset.describe()[columnname]["max"]
            descriptive[columnname]["IQR"]=descriptive[columnname]["Q3=75%"]-descriptive[columnname]["Q1=25%"]
            descriptive[columnname]["1.5rule"]=1.5*descriptive[columnname]["IQR"]
            descriptive[columnname]["Lowest"]=descriptive[columnname]["Q1=25%"]-descriptive[columnname]["1.5rule"]
            descriptive[columnname]["Greatest"]=descriptive[columnname]["Q3=75%"]+descriptive[columnname]["1.5rule"]
            descriptive[columnname]["Min"]=dataset[columnname].min()
            descriptive[columnname]["Max"]=dataset[columnname].max()
        return descriptive
    
    def outlierFound(descriptive):
        lowest=[]
        higher=[]
        for columnname in descriptive.columns:
            if(descriptive[columnname]["Min"]<descriptive[columnname]["Lowest"]):
                lowest.append(columnname)
            if(descriptive[columnname]["Max"]>descriptive[columnname]["Greatest"]):
                higher.append(columnname)
        return lowest,higher
    
    def outlierReplace(lowest,higher,dataset,descriptive):
        for columnname in lowest:
            dataset[columnname][dataset[columnname]<descriptive[columnname]["Lowest"]]=descriptive[columnname]["Lowest"]
        for columnname in higher:
            dataset[columnname][dataset[columnname]>descriptive[columnname]["Greatest"]]=descriptive[columnname]["Greatest"]
        return dataset
