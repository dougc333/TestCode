
import sys
import pandas as pd
import numpy as np

class KNN(object):
  def __init__(self):
    self.df = None
    self.samp = None

  def load_data(self,expfile, sampfile):
    #True for knn
    self.df = self.load_expression_data(expfile,True)
    self.samp= self.load_samples(sampfile)
    
  def get_assignments(self,k, fn):
    '''
    input:k nearest neighbirs, fn fraction
    output:return list of integer 0 and 1. 
    '''
    self.k = k
    self.fn = fn
    healthy_dis = self.get_scores(k,fn)
    #print("get_assignments healthy_dis:",healthy_dis)
    #autoshamer requires order of patients same as samples file
    autoshamer = {}
    assignment_list = []
    for idx in range(0,len(healthy_dis)):
      subject = healthy_dis[idx][0]
      status = healthy_dis[idx][1]
      autoshamer[subject]=status
    #print("autoshamer dict:",autoshamer)
    for x in self.samp.keys():
      assignment_list.append(autoshamer[x])
    #print("assignment_list after autoshamer:",assignment_list)
    return assignment_list

  def load_expression_data(self,file_name,drop):
    '''
    input: gene expression filename
    output: pandas dataframe
    '''
    df = pd.read_csv(file_name,sep='\t')
    if drop:
        df = df.drop(columns='SYMBOL')
    #print(df.head())
    return df

  def load_samples(self,file_name):
    '''
    input: filename of samples
    output: distionary, key=patient name, value=0 healthy, 1 diseased
    '''
    d = {}
    with open(file_name, "r") as fh:
        lines = fh.readlines()
        for line in lines:
            tokens = line.split()
            d[tokens[0]] = tokens[1]
    #print("d:",d)
    return d

  def get_scores(self,k,fn):
    '''
    input: gene expression file for patients defined as columns in text file
    output: list of 0 and 1, one value for each column in input file
    '''
    #df = load_expression_data(filename,True)
    healthy_dis = []
    for col in self.df.columns:
        #print(col)
        one = self.df.loc[:, self.df.columns == col]
        rest_minus_one = self.df.loc[:,self.df.columns!=col]
        #print(one.columns)
        #print("---single---")
        #print(one.head())
        #print(rest_minus_one.columns)
        #print("---rest----")
        #print(rest_minus_one.head())
        healthy_dis.append(self.get_dist(one,rest_minus_one,k,fn))
    #print("get_scores healthy_dis:",healthy_dis)
    #return a y_true
    return healthy_dis
  
  def get_dist(self,one,rest,k,fn):
    '''
    input: single patient as one, rest of patients as rest
    output: 1 if one is diseaased, 0 if healthy
    '''
    #print(one.shape,rest.shape)
    dist_list = []
    for idx in range(0,(rest.shape)[1]):
        #print("one shape",one.shape,"one column:",one.columns[0])
        #print("one:",one.to_numpy(),type(one.to_numpy()))
        #print("rest shape:",rest.to_numpy()[:,idx].shape,"rest column name:",rest.columns[idx])
        #print("rest_column:",rest.to_numpy()[:,[idx]],type(rest.to_numpy()[:,[idx]]))
        dist = np.linalg.norm(one.to_numpy()-rest.to_numpy()[:,[idx]])
        #print("dist:",dist)
        dist_list.append((one.columns[0],rest.columns[idx],dist))
    #print("dist_list:",dist_list)
    #print("*****sorting*****")
    lowest_first = sorted(dist_list,key=lambda x :x[2])
    #print(lowest_first)
    #do we round down or round up? 
    lowest_first_filtered = lowest_first[0:(k)]
    #print("k closest:",lowest_first_filtered)
    #for each sample in dist_list, is this sample,one healthy or diseased? 
    num_dis=0
    for tupl in lowest_first_filtered:
        #print("processing:",tupl, "one:",tupl[0],"compare:",tupl[1],"samp(compare):",self.samp[tupl[1]],type(self.samp[tupl[1]]))
        if self.samp[tupl[1]]=="1":
            #print("*** DISEASED!!!***")
            num_dis +=1
    #print("num_dis:",num_dis,"k*fn:",k*fn)
    if num_dis > k*fn:
        return (one.columns[0],1)
    return (one.columns[0],0)
  
  def calc_error(self,healthy_dis,samp):
    '''
    input: predicted and actual
    output: tpr, fpr for 1 sample
    '''
    num_correct=0
    num_incorrect=0
    tp_one = 0
    fp_zero = 0
    fn_one = 0
    tn_zero = 0
    for idx in range(0,len(healthy_dis)):
        subject = healthy_dis[idx][0]
        status = healthy_dis[idx][1]
        #print(type(status),type(subject),"status:",status," subject:",subject)
        if(status)==int(samp[subject]):
            num_correct+=1
        else:
            num_incorrect+=1
        if int(samp[subject])==1 and status==1:
            tp_one+=1
        elif(int(samp[subject])==1 and status==0):
            fn_one+=1
        elif(int(samp[subject])==0 and status==1):
            fp_zero+=1
        elif(int(samp[subject])==0 and status==0):
            tn_zero+=1
        else:
            print("should not see this")
            sys.exit()
    #print("num_correct:",num_correct," num_incorrect:",num_incorrect)
    #print("tp_one:",tp_one," fn_one:",fn_one," fp_zero:",fp_zero," tn_zero:",tn_zero)
    tpr = tp_one/(tp_one+fn_one)
    fpr = fp_zero/(fp_zero+tn_zero)
    #print("tpr:",tpr," fpr:",fpr)
    #print("sensitivity:",tpr, "specifity:",1-fpr)
    #print("accuracy:",(tp_one+tn_zero)/len(healthy_dis)) #need to return this or the tp,fn stats
    sens = tpr
    spec = 1-fpr
    return [sens, spec]
    

  def calc_metrics(self,k, fn):
    '''
    return sensitivity and specifity
    ''' 
    healthy_dis = self.get_scores(k,fn)
    #print("calc metric healthy_dis:",healthy_dis)
    #careful this is a list. this is no longer out tuple. 
    num_correct=0
    num_incorrect=0
    tp_one = 0
    fp_zero = 0
    fn_one = 0
    tn_zero = 0
    actual=[]
    misclassified={}
    for idx in range(0,len(healthy_dis)):
        subject = healthy_dis[idx][0]
        status = healthy_dis[idx][1]
        #print(type(status),type(subject),"status:",status," subject:",subject)
        #actual.append(int(self.samp[subject]))
        if(status)==int(self.samp[subject]):
            num_correct+=1
        else:
            num_incorrect+=1
        if int(self.samp[subject])==1 and status==1:
            tp_one+=1
        elif(int(self.samp[subject])==1 and status==0):
            fn_one+=1
            #print(subject+"fn")
            #if self.samp[subject] not in misclassified.keys():
            #  misclassified[self.samp[subject]]=1
            #else:
            #  misclassified[self.samp[subject]]+=1
        elif(int(self.samp[subject])==0 and status==1):
            fp_zero+=1
            #print(subject+"fp")
            #if self.samp[subject] not in misclassified.keys():
            #  misclassified[self.samp[subject]]=1
            #else:
            #  misclassified[self.samp[subject]]+=1
        elif(int(self.samp[subject])==0 and status==0):
            tn_zero+=1
        else:
            print("should not see this")
            sys.exit()
    #print("num_correct:",num_correct," num_incorrect:",num_incorrect)
    #print("tp_one:",tp_one," fn_one:",fn_one," fp_zero:",fp_zero," tn_zero:",tn_zero)
    tpr = tp_one/(tp_one+fn_one)
    fpr = fp_zero/(fp_zero+tn_zero)
    #print(misclassified)
    #print("tpr:",tpr," fpr:",fpr)
    #print("actual:",actual)
    #print("healthy_sis:",[x[1] for x in healthy_dis])
    #print("sensitivity:",tpr, "specifity:",1-fpr)
    #print("accuracy:",(tp_one+tn_zero)/len(healthy_dis)) #need to return this or the tp,fn stats
    sens = tpr
    spec = 1-fpr
    #return tpr,fpr
    return [sens, spec]

if __name__ == "__main__":
  exp_file = sys.argv[1]
  samp_file = sys.argv[2]
  knn=KNN()
  knn.load_data(exp_file,samp_file)
  al = knn.get_assignments(5,0.5)
  print("al:",al)
  foo = knn.calc_metrics(5,0.5)
  print("foo:",foo)
  roc=[]
  #create ROC curve from above. write to file and use jupyter notebook
  '''
  one = knn.calc_metrics(3,.05)
  two = knn.calc_metrics(3,0.1)
  three = knn.calc_metrics(3,0.25)
  four = knn.calc_metrics(3,0.5)
  five = knn.calc_metrics(3,0.75)
  six = knn.calc_metrics(3,0.9)
  seven = knn.calc_metrics(3,1.0)
  
  #print out accuracy and types of misclassification. greater than 3. 
  
  first = knn.calc_metrics(1,0.5)
  second = knn.calc_metrics(2,0.5)
  third = knn.calc_metrics(3,0.5)
  fourth = knn.calc_metrics(4,0.5)
  fifth = knn.calc_metrics(5,0.5)
  sixth = knn.calc_metrics(6,0.5)
  '''