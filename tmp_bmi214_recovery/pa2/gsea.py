import sys
import pandas as pd
import numpy as np

class GSEA:
    def __init(self):
        self.df=None
        self.samp=None
        self.expr_gene=None
        self.pathway_gene_dict = None
        self.ref = {}

    def load_expression_data(self,file_name,drop):
        '''
        input: gene expression filename
        output: pandas dataframe
        '''
        df = pd.read_csv(file_name,sep='\t')
        if drop:
            df = df.drop(columns='SYMBOL')
        return df

    def get_expression_genes(self,df):
        '''
        input: dataframe
        output: list of genes, 10712
        '''
        df_small = df.iloc[:,df.columns=="SYMBOL"]
        gene_list = df_small.to_numpy().flatten()
        return gene_list 

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
        return d
    
    def load_kegg(self,filename):
        '''
        input:kegg file name
        output: dictionary key=KEGG_CITRATE_CYCLE_TCA_CYCLE value=list of genes which are in expression data
        all_genes all genes in all pathways no screening
        hum_genes, only count ones in expression file
        glist only count ones in expression file. glist/path_gene and hum_genes difference? pathgene dict of pathway, list of genes in expressoin
        '''
        path_gene = {}
        with open(filename, "r") as fh:
            lines = fh.readlines()
            #print("len(lines):",len(lines))
            for i in range(0,len(lines)):
                tokens = lines[i].split()
                genes = tokens[2:]
                g_list=[]
                for g in genes:
                    #print("+++++++++++testing g:",g)
                    if g in self.expr_gene:
                        #print("g is in self.expr_gene!!!!!")
                        g_list.append(g)
                        #if gene in expression data add to hum_gene dict
                #if i==0:
                    #print("len g_list, should match later query:",len(g_list))
                path_gene[tokens[0]] = g_list
                #path_gene[tokens[0]] =tokens[2:]
                #print("pathway:",tokens[0]," num genes:",len(g_list))
            #print(" len path_gene:",len(path_gene))
            return path_gene

    
    def load_data(self,expfile,sampfile,keggfile):
        self.samp = self.load_samples(sampfile)
        self.df = self.load_expression_data(expfile,False)       
        self.expr_gene = self.get_expression_genes(self.df)
        self.pathway_gene_dict = self.load_kegg(keggfile)
        

    def get_gene_rank_order(self):
        #print("get_gene_rank_order")
        #print("------df head--------")
        #print(self.df.head())
        #print("---------------------")
        rows,cols = self.df.shape
        #build healthy and diseased indexes
        #print(self.df.columns)
        healthy_idx=[]
        disease_idx=[]
        for idx,col in enumerate(self.df.columns):
            #print("idx:",idx," col:",col)
            #print(self.samp)
            if col!="SYMBOL":
                #print("idx:",idx,"col:",col,self.samp[col])
                if self.samp[col]=='1':
                    disease_idx.append(idx)
                elif self.samp[col]=='0':
                    healthy_idx.append(idx)
                else:
                    print("xxxx")

        #print("healthy_idx:",healthy_idx," disease_idx:",disease_idx)
        df_np = self.df.to_numpy()
        #print("rows:",rows,"cols:",cols)#fetch healthy as list of columns, diseased as list of columns
        rank_me=[]
        healthy_mean=np.mean(df_np[0,[healthy_idx]])
        disease_mean=np.mean(df_np[0,[disease_idx]])
        for idx in range(0,df_np.shape[0]):
            #print("df iloc:",df.iloc[idx,0],df_np[0,[healthy_idx]],healthy_mean)
            #print(df_np[0,[disease_idx]],disease_mean)
            #print("diff:",disease_mean-healthy_mean)
            healthy_mean=np.mean(df_np[idx,[healthy_idx]])
            disease_mean=np.mean(df_np[idx,[disease_idx]])
            rank_me.append((idx,self.df.iloc[idx,0],disease_mean-healthy_mean)) #sort by second tuple value

        #print("length ranked genes: ",len(rank_me))
        #before sorting
        #print("rank_me[0:5]",rank_me[0:5])
        largest_first = sorted(rank_me, key = lambda x: x[2],reverse=True)
        #print("largest_first[0:5]",largest_first[0:5],len(largest_first))
        #return list of genes only largest first
        return_me=[]
        for x in largest_first:
            return_me.append(x[1])
        #print("return_me[0:5]:",return_me[0:5],len(return_me))
        return return_me
    
    def get_enrichment_score(self,geneset):
        largest = self.get_gene_rank_order()
        #print("get enrichment score:",geneset)
        
        ng = len(self.pathway_gene_dict[geneset])
        nt= len(self.expr_gene)
        penalty_add =np.sqrt((nt-ng)/ng)
        penalty_miss = np.sqrt(ng/(nt-ng))
        #print("ng:",ng," penalty_add:",penalty_add," penalty_miss:",penalty_miss)    
        #calculate ES for each geneset pathway_gene_dict[x] using ranked list. wow for all 10k? 
        es=[]
        es.append(0.)
        sum_es=0.
        for idx in range(0,len(largest)):
            #print(idx,"processing gene:",self.largest[idx])
            #this is right list? not largest first??? wait the geneset has to be in expressoin data
            if largest[idx] in self.pathway_gene_dict[geneset]:
                sum_es +=penalty_add
            else:
                sum_es-=penalty_miss
            es.append(sum_es)
        #print("es:",es)
        #print("es max:",max(es),round(max(es),2))
        return round(max(es),2)
    
    def calc_all_es(self):
        '''
        input: self.pathway_gene_dict
        output: self.ref enrichment scores for all kegg pathways
        '''
        ref={}
        for x in self.pathway_gene_dict.keys():
            es = self.get_enrichment_score(x)
            #print("pathway:",x, "has es:",es)
            ref[x] = es
        #print(ref)
        return ref 

    def get_gene_rank_order_permute(self):
        '''
        each call to this returns a different gene ordering a single
        permutation
        '''
        #print("get_gene_rank_order_permute")
        #print("------df head--------")
        #print(self.df.head())
        #print("---------------------")
        ind = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
        np.random.shuffle(ind)
        healthy_idx=ind[0:6]
        disease_idx=ind[7:14]

        #print("permute healthy_idx:",healthy_idx," permute disease_idx:",disease_idx)
        
        df_np = self.df.to_numpy()
        #print("rows:",rows,"cols:",cols)#fetch healthy as list of columns, diseased as list of columns
        rank_me=[]
        healthy_mean=np.mean(df_np[0,[healthy_idx]])
        disease_mean=np.mean(df_np[0,[disease_idx]])
        for idx in range(0,df_np.shape[0]):
            #print("df iloc:",df.iloc[idx,0],df_np[0,[healthy_idx]],healthy_mean)
            #print(df_np[0,[disease_idx]],disease_mean)
            #print("diff:",disease_mean-healthy_mean)
            healthy_mean=np.mean(df_np[idx,[healthy_idx]])
            disease_mean=np.mean(df_np[idx,[disease_idx]])
            rank_me.append((idx,self.df.iloc[idx,0],disease_mean-healthy_mean)) #sort by second tuple value

        #print("length ranked genes: ",len(rank_me))
        #before sorting
        #print("rank_me[0:5]",rank_me[0:5])
        largest_first = sorted(rank_me, key = lambda x: x[2],reverse=True)
        #print("largest_first[0:5]",largest_first[0:5],len(largest_first))
        #return list of genes only largest first
        return_me=[]
        for x in largest_first:
            return_me.append(x[1])
        #print("return_me[0:5]:",return_me[0:5],len(return_me))
        return return_me


    def get_permute_enrichment_score(self,geneset,largest):
        #print("permute ranked genes:",largest[0:5])
        #print("get_permute_enrichment_score:",geneset)
        
        ng = len(self.pathway_gene_dict[geneset])
        nt= len(self.expr_gene)
        penalty_add =np.sqrt((nt-ng)/ng)
        penalty_miss = np.sqrt(ng/(nt-ng))
        #print("ng:",ng," penalty_add:",penalty_add," penalty_miss:",penalty_miss)    
        #calculate ES for each geneset pathway_gene_dict[x] using ranked list. wow for all 10k? 
        es=[]
        es.append(0.)
        sum_es=0.
        for idx in range(0,len(largest)):
            #print(idx,"processing gene:",self.largest[idx])
            #this is right list? not largest first??? wait the geneset has to be in expressoin data
            if largest[idx] in self.pathway_gene_dict[geneset]:
                sum_es +=penalty_add
            else:
                sum_es-=penalty_miss
            es.append(sum_es)
        #print("es:",es)
        #print("es max:",max(es),round(max(es),2))
        return round(max(es),2)


    def get_sig_sets(self,p):
        #correct for #genesets
        ref = self.calc_all_es()
        bigger = {}
        for x in range(0,10):
            largest = self.get_gene_rank_order_permute()
            p = p/len(self.pathway_gene_dict.keys())
            for x in self.pathway_gene_dict.keys(): 
                permute_es = self.get_permute_enrichment_score(x,largest)
                #print(x,"permute_es:",permute_es, "ref_es:",ref[x])
                if permute_es > ref[x]:
                    if x not in bigger.keys():
                        bigger[x] = 1
                    else:
                        bigger[x]+=1
        #print("bigger:",bigger)
        #print genesets in bigger
        return_list = []
        #correct for p value
        for x in bigger.keys():
            if bigger[x]/100. > p:
                return_list.append(self.pathway_gene_dict[x])
        #print("return_list:",return_list)
        return []

    def q10(self):
        """
        which geneset has highest ES? KEGG_NEUROACTIVE_LIGAND_RECEPTOR_INTERACTION
        """
        score=[]
        for x in self.pathway_gene_dict.keys():
            s = self.get_enrichment_score(x)
            score.append(s)
            print("processing:",x," ES:",s)
        print("q10 max:",max(score))
        
    def q12(self):
        """
        how many unique genes in kegg file
        """
        g=[]
        for x in self.pathway_gene_dict.keys():
            genes = self.pathway_gene_dict[x]
            #print("pathway:",x," genes:",genes)
            g.extend(genes)
        set_genes=set(g)
        print("num genes:",len(g),"num unique:",len(set_genes))
        
        
if __name__ == "__main__":
    exp_file = sys.argv[1]
    samp_file = sys.argv[2]       
    kegg_file = sys.argv[3]
    gsea=GSEA()
    gsea.load_data(exp_file,samp_file,kegg_file)
    #this mirrors self.largest set in class
    l = gsea.get_gene_rank_order()
    #print("rank order:",len(l),l[0:5])
    #print(gsea.get_enrichment_score("KEGG_CITRATE_CYCLE_TCA_CYCLE"))
    gsea.get_sig_sets(.05)

    #gsea.q10()
    #print("*********")
    #gsea.q12()

