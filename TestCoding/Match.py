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
    dictTerms= {"PO":"oral", "or":"oral","\"":""}
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
        
        handler = logging.FileHandler('/Users/dc/TestCode/TestCoding/match.log', 'a')
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
            self.processBase(query[0:findParen])
            self.processBase(query[findParen+1:query.find(")")])
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
            print "processBase needOneTermStats q:%s" % q
            self.logger.info("processBase needOneTermStats q:%s" % q)
            self.c.execute(q)
            result = self.c.fetchall()
            self.resultStatsQ[self.numQueriesProcessed] = len(result)
            for r in result:
                self.logger.info("processBase needOneTermStats r:%s", r)
            print "oneTermStats num result:%d" , len(result)
            if (len(result)==0):
                self.numOneTermZeroResults +=1
                
                
        if (self.bagOfWords):
            terms = cleanQ.split()
            print "bagWords terms:", terms
            self.cleanTerms(terms)
            print "bagWords after replacement", terms 
            q = "select * from lookup where name like \'%"+terms[0]+"%\'"
            print "processBase bagWords q:%s" % q
            self.logger.info("processBase bagWords q:%s" % q)
            self.c.execute(q)
            result = self.c.fetchall()
            self.resultStatsBOW[self.numQueriesProcessed] = len(result)

            #for r in result:
            #    self.logger.info("processBase bagWords r:%s", r)
            print "bagWords num baseResult:%d" , len(result)
            self.logger.info("bagWords num baseResult:%d" , len(result))
            if (len(result)==0):
                self.numBagWordsZeroResults +=1
                self.logger.info("BOW 0 RESULTS")
            #pick out best query matches
        return       
        
       
    def cleanTerms(self, terms):
        """
        replace terms with dict
        """                            
        for index in range(len(terms)):
            print index
            print terms[index]
            if terms[index] in self.dictTerms:
                print "terms[index] in dictTerms"
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
        print "self.numQueriesProcessed:%d" % self.numQueriesProcessed
        if (self.needOneTermStats):
            print "self.numOneZeroResults:%d" % self.numOneTermZeroResults
            print self.resultStatsQ
            
        if(self.bagOfWords):
            print "bagWords numBagWordsZeroResults:%d" % self.numBagWordsZeroResults
            print self.resultStatsBOW
m = Match()
m.test()
m.close()

