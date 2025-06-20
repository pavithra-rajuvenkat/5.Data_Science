class QuanQual():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnNames in dataset.columns:
            if(dataset[columnNames].dtype=='O'):
                qual.append(columnNames)
            else:
                quan.append(columnNames)
        return quan,qual
