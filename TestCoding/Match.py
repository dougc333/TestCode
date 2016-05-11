#!/usr/bin/python

import sqlite3
import re
import logging
from collections import defaultdict
from __builtin__ import True

#recall @50% improve recall
class Match(object):
    conn = sqlite3.connect('/Users/dc/TestCode/TestCoding/clinical.sqlite')
    c=conn.cursor()
    dictTerms= {"PO":"oral","po":"oral", "or":"oral","\"":""}
    needOneTermStats = True
    bagOfWords = True
    numOneTermZeroResults = 0
    numBagWordsZeroResults = 0
    numQueriesProcessed = 0
    
    resultStatsQ = defaultdict(int)
    resultStatsBOW = defaultdict(int)
    
    def __init__(self):
        #for ipython only...
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("do you see me in red? testing root logger")
        print self.logger.handlers
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)
        #end ipython
        
        handler = logging.FileHandler('/Users/dc/TestCode/TestCoding/match.log', 'w')
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.info("match init")        
        self.firstQueryResult = []
        self.parenResult = []
        
    def processQuery(self,query):
        #removeParen = re.sub(r"[\(\)]", "", self.cleanQuery(query))
        #self.baseResult = self.processBase(removeParen)
        self.numQueriesProcessed += 1
        
        findParen = query.find("(")
        if findParen != -1:
            #split into 2 queries
            self.processBase(query[0:findParen],query[findParen+1:query.find(")")])
            #in some cases we have process the paren term as a separate base term
            #self.processBase(query[findParen+1:query.find(")")])
        else:
            self.firstQueryResult = self.processBase(query,"")
            
        
    def processBase(self,query,parenString):
        """
        2 cases for documentation
        1) treat query as single query term. Problem is longer query strings have higher probability of 0 results
        2) break apart query into first term and treat as bag of words narrowing scope using BOW. Problem first term has too many results
        3) do BOW only if single query term has 0 results. 
        """
        
        print "processBase query:%s" % query
        self.logger.info("processBase query:%s" % query)
        
        cleanQ = self.cleanPunct(query)
        #baseTerms = cleanQ.split()
        #baseTerms["po"] = "oral"
        print "processBase cleanQ:%s" % cleanQ
        self.logger.info("processBase cleanQ:%s" % cleanQ)
            
        if (self.needOneTermStats):   
            q = "select * from lookup where name like \'%"+cleanQ+"%\'"
            qCount = "select distinct(rxcui) from lookup where name like \'%"+cleanQ+"%\'"
            #q = "select * from lookup where name like \'%"+baseTerms[0]+"%\'"        
            print "processBase needOneTermStats q:%s" % q
            self.logger.info("processBase needOneTermStats q:%s" % q)
            self.c.execute(q)
            result = self.c.fetchall()
            self.resultStatsQ[self.numQueriesProcessed] = len(result)
            for r in result:
                self.logger.info("processBase needOneTermStats r:%s", r)
                print "needOneTermStats result:", r
            print "oneTermStats num result:%d" , len(result)
            self.logger.info("oneTermStats num result:%d" , len(result))
            
            self.c.execute(qCount)
            resultNumRXCUI = self.c.fetchall()
            print "numDistinct rxcui:%d for cleanQ:%s" % (len(resultNumRXCUI),cleanQ)
            self.logger.info("numDistinct rxcui:%d for cleanQ:%s" % (len(resultNumRXCUI),cleanQ))
            
            if (len(result)==0):
                self.numOneTermZeroResults +=1
            else:
                """
                """
                print "parenString:%s" % parenString
                self.logger.info( "parenString:%s" % parenString)
                cleanParenString=self.cleanPunct(parenString)
                print "cleanParenString:%s" % cleanParenString
                self.logger.info( "cleanParenString:%s" % cleanParenString)
                termParen=cleanParenString.split()
                self.cleanTerms(termParen)
                print "termParen:", termParen
                self.logger.info( "termParen:")
                self.logger.info(" ".join(termParen))
                self.numTrue=0
                self.filterResult(result,termParen)
                print "----------------------"
                print "numTrue:%d" % self.numTrue
                self.logger.info("numTrue:%d" % self.numTrue)
                print "----------------------"
        
        """
        add parenString to terms, cleanPunct, lowercase, split
        """        
        if (self.bagOfWords):
            terms = cleanQ.split()
            print "bagWords terms:", terms
            self.logger.info("bagWords terms:")
            self.logger.info(" ".join(terms))
            self.cleanTerms(terms)
            print "bagWords after replacement", terms 
            q = "select * from lookup where name like \'%"+terms[0]+"%\'"
            print "processBase bagWords q:%s" % q
            self.logger.info("processBase bagWords q:%s" % q)
            self.c.execute(q)
            result = self.c.fetchall()
            #print "---------------"
            #print result
            #print "---------------"
            
            self.resultStatsBOW[self.numQueriesProcessed] = len(result)

            print "bagWords num baseResult:%d" , len(result)
            self.logger.info("bagWords num baseResult:%d" , len(result))
            if (len(result)==0):
                self.numBagWordsZeroResults +=1
                self.logger.info("BOW 0 RESULTS")
            else:
                self.logger.info("calling filterResult:")
                for t in terms:
                    self.logger.info("terms:%s", t)
                self.filterResult(result , terms)
        return       
    
    
        
    def filterResult(self,rTupleList, terms):
        """
        input: resultList from first term like, term list
        output: filtered resultList matching all terms
        """
        print "calling filterResult"
        print "numResults:%d" % len(rTupleList)
        self.logger.info("calling filterResult")
        self.logger.info("-----------------------")
        #self.logger.info("rList:"+rList)
        self.logger.info("-----------------------")
        
        
        for rTuple in rTupleList:
            #self.logger.info("resultString:%s" % rTuple[0])
            
 #           print "rxcui:%s" % rTuple[1]
            #self.logger.info("rxcui:%s" % rTuple[1])
            
            
  #          print "processing match for:%s" % rTuple[0].split()
            #self.logger.info("processign match for r:%s" % rTuple[0].split())
   #         print "matching term:", terms
            #self.logger.info("matching term:", terms)
    #        print "set(terms):", set(terms)
            #self.logger.info("set(terms):", str(set(terms)))
     #       print "set(r):", set(rTuple[0].split())
            #self.logger.info("set(r):", str(set(rTuple[0].split())))
            trueOrFalse = set(terms).issubset(set(rTuple[0].split()))
            if trueOrFalse==True:
                self.numTrue+=1
                #print "resultString:%s" % rTuple[0]
                self.logger.info("resultString:%s" % rTuple[0])               
                #print "set(r) is subset:", trueOrFalse
                self.logger.info( "set(r) is subset:%s", str(trueOrFalse))
            
            
    def cleanTerms(self, terms):
        """
        replace terms with dict
        """                            
        for index in range(len(terms)):
            #print "cleanTerms index:%d" % index
            #print "cleanTerms: %s" % terms[index]
            if terms[index] in self.dictTerms:
             #   print "terms[index] in dictTerms"
                foo = self.dictTerms[terms[index]]
                terms[index] = foo 
        
        
    def cleanPunct(self,query):
        """
        removes punctuation:
        replace - with space, have to be careful with the hyphen. Sometimes this is not correct
        replace ' with nothing
        """
        print "query before clean punct:%s" % query
        self.logger.info("query before clean punct:%s" % query)
        replaceSpace = re.sub("[-|/,]"," ",query.lower())
        self.logger.info("replaceSpace:%s", replaceSpace)
        cleanPunct = re.sub("['[\],]*", "", replaceSpace).strip()
        print "clean punct:%s" % cleanPunct
        self.logger.info("clean punct:%s" % cleanPunct)
        return cleanPunct
    
    def test(self):
        with open("/Users/dc/TestCode/TestCoding/nomatch.csv") as f:
            for x in range(5):
                for line in f:
                    print line
                    self.processQuery(line)
    
    
    def writeToCSV(self,fileWrite,dict):
        for keys in dict:
            fileWrite.write(str(keys)+":"+str(dict[keys]))
            fileWrite.write("\n")
        fileWrite.close()
        
                    
    def close(self):        
        print "self.numQueriesProcessed:%d" % self.numQueriesProcessed
        if (self.needOneTermStats):
            print "self.numOneZeroResults:%d" % self.numOneTermZeroResults
            print self.resultStatsQ
            self.writeToCSV(open("/Users/dc/TestCode/TestCoding/statsQ.txt","w"), self.resultStatsQ)
            
        if(self.bagOfWords):
            print "bagWords numBagWordsZeroResults:%d" % self.numBagWordsZeroResults
            print self.resultStatsBOW
            self.writeToCSV(open("/Users/dc/TestCode/TestCoding/BOW.txt","w"), self.resultStatsBOW)
            
m = Match()
m.test()
m.close()

