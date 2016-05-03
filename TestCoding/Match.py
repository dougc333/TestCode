#!/usr/bin/python

import sqlite3
import re
import logging
import sys
from __builtin__ import True

#recall @50% improve recall
class Match(object):
    conn = sqlite3.connect('/Users/dc/TestCode/TestCoding/clinical.sqlite')
    c=conn.cursor()
    dictTerms= {"PO":"oral", "or":"oral","\"":""}
    needOneTermStats = True
    bagOfWords = True
    numOneTermZeroResults = 0
    
    def __init__(self):
        #for ipython only...
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("do you see me in red? testing root logger")
        print self.logger.handlers
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)
        #end ipython
        
        handler = logging.FileHandler('/Users/dc/TestCode/TestCoding/match.log', 'a')
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.info("match init")        
        self.firstQueryResult = []
        self.parenResult = []
        
        
    def processQuery(self,query):
        #removeParen = re.sub(r"[\(\)]", "", self.cleanQuery(query))
        #self.baseResult = self.processBase(removeParen)
        
        findParen = query.find("(")
        if findParen != -1:
            #split into 2 queries
            self.firstQueryResult = self.processBase(query[0:findParen])
            print "found paren numBaseResult:%d" % len(self.firstQueryResult) 
            self.logger.info( "found paren numBaseResult:%d" % len(self.firstQueryResult)) 
            self.parenResult = self.processBase(query[findParen+1:query.find(")")])
        else:
            self.firstQueryResult = self.processBase(query)
            
        
    def processBase(self,query):
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
            #q = "select * from lookup where name like \'%"+baseTerms[0]+"%\'"        
            print "processBase q:%s" % q
            self.logger.info("processBase q:%s" % q)
            self.c.execute(q)
            result = self.c.fetchall()
            for r in result:
                self.logger.info("processBase r:%s", r)
            print "oneTermStats num baseResult:%d" , len(result)
            if (len(result)==0):
                self.numOneTermZeroResults +=1
                
        if (self.bagWords):
            #generate terms list and process first term then narrow recall. first document 100% recall
            terms = cleanQ.split()
            print "bagWords terms:"
        
        
        
        
        return result
        
        #print "setBaseResult:%d", len(set(self.baseResult))
        
                
        #qDistinct = "select distinct(rxcui) from lookup where name like \'%"+cleanQ+"%\'"
        #print "distinctQuery:%s" % qDistinct
        #self.logger.info("distinctQuery:%s" % qDistinct)
        #self.c.execute(qDistinct)
        #distinctResult = self.c.fetchall()
        #print "numDistinct:%d", len(distinctResult)
        #print "set numDistinct:%d", len(set(distinctResult))
        #self.logger.info("numDistinct:%d", len(distinctResult))
        #self.logger.info("set numDistinct:%d", len(set(distinctResult)))
        
        
    def processParen(self,query):
        """
        using ferrous sulfate example the paren terms are a separate set and have to
        be anded with the original terms. Return list with best match and put on top. 
        refactor this out. only need the replacement of po w/oral or or w/oral.
        add the dictionary processing on terms 
        """
        print "processParen query:%s" % query
        self.logger.info("processParen query:%s" % query)
        terms = self.cleanQuery(query).split()
        print "processParen terms:%s" % terms
        self.logger.info("processParen terms:%s" % terms)
        poExists=False
        if "po" in terms:
            terms.remove("po")
            poExists = True
        
        qTerms = " ".join(terms)
        qString = "select * from lookup where name like '%"+qTerms+"%'"
        print "processParen qString:%s" % qString
        self.logger.info("processParen qString:%s" % qString)
        self.c.execute(qString)
        self.parenResult=self.c.fetchall()
        print "numResults self.parenResult:%d" % len(self.parenResult)
        print "numDistinct self.parenResult:%d" % len(set(self.parenResult))
        self.logger.info("numResults self.parenResult:%d" % len(self.parenResult))
        self.logger.info("numDistinct self.parenResult:%d" % len(set(self.parenResult)))
        distinctString = "select distinct(rxcui) from lookup where name like '%"+qTerms+"%'"
        print "distinctString:%s" % distinctString
        self.logger.info("distinctString:%s" % distinctString)
        self.c.execute(distinctString)
        distinctResult = self.c.fetchall()
        print "numDistinct:%d" % len(distinctResult)
        print "set numDistinct:%d" % len(set(distinctResult))
        self.logger.info("numDistinct:%d" % len(distinctResult))
        self.logger.info("set numDistinct:%d" % len(set(distinctResult)))
        
        
        for r in set(self.parenResult):
            print r
#            self.logger.info(r)
        for r in set(self.parenResult):
            if poExists:
                terms.append("oral")
            print "single parenResult: " , r , "numTuples:", len(r), "name tokens:", r[0].split(), "set r[0]:" , set(r[0].split())
            print "set terms:" , set(terms)
 #          self.logger.info()
 #          self.logger.info()
            print set(terms).issubset(set(r[0].split()))
 #          self.logger.info()
       
    def cleanTerms(self, terms):
        """
        replace terms with dict
        """                            
        for key in self.dictTerms:
            if key in terms:
                terms[key] = self.dictTerms[key] 
        
        
    def cleanPunct(self,query):
        """
        removes punctuation:
        replace - with space, have to be careful with the hyphen. Sometimes this is not correct
        replace ' with nothing
        """
        print "query before clean punct:%s" % query
        self.logger.info("query before clean punct:%s" % query)
        replaceSpace = re.sub("-"," ",query.lower())
        cleanPunct = re.sub("'", "", replaceSpace).strip()
        print "clean punct:%s" % cleanPunct
        self.logger.info("clean punct:%s" % cleanPunct)
        return cleanPunct
    
    def test(self):
        with open("/Users/dc/TestCode/TestCoding/nomatch.csv") as f:
            for x in range(5):
                for line in f:
                    print line
                    self.processQuery(line)
                    
    def close(self):
        print "numBaseResult:%d" % self.numBaseResult
        if (self.needOneTermStats):
            print "self.numOneTermStats:%d" % self.numOneTermZeroResults
    
m = Match()
m.test()
m.close()

