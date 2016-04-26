#!/usr/bin/python

import sqlite3
import re
import logging
import sys

class Match(object):
    conn = sqlite3.connect('/Users/dc/TestCode/TestCoding/clinical.sqlite')
    c=conn.cursor()
    
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("do you see me in red? testing root logger")
        print self.logger.handlers
        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)
        
        handler = logging.FileHandler('/Users/dc/TestCode/TestCoding/match.log', 'a')
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)
        self.logger.info("match init")        
        self.baseResult = []
        self.ParenResult = []
        self.matchResult= []
        self.zeroBaseResult=0
        self.numBaseResult = 0
        
    def processQuery(self,query):
        findParen = query.find("(")
        if findParen != -1:
            self.processBase(query[0:findParen])
            print "found paren numBaseResult:%d" % len(self.baseResult) 
            self.logger.info( "found paren numBaseResult:%d" % len(self.baseResult)) 
            self.processParen(query[findParen+1:query.find(")")])
        else:
            self.baseResult = self.processBase(query)
            
        
    def processBase(self,query):
        cleanQ = self.cleanBaseQuery(query)
        print "processBase query:%s" % cleanQ
        self.logger.info("processBase query:%s" % cleanQ)
        q = "select * from lookup where name like \'%"+cleanQ+"%\'"
        print "processBase q:%s" % q
        self.logger.info("processBase q:%s" % q)
        self.c.execute(q)
        self.baseResult = self.c.fetchall()
        print "num baseResult:%d" , len(self.baseResult)
        print "setBaseResult:%d", len(set(self.baseResult))
        
        if len(self.baseResult) == 0:
            self.zeroBaseResult+=1
        else:
            self.numBaseResult += 1
        
        self.logger.info("num baseResult:%d" , len(self.baseResult))
        self.logger.info("setBaseResult:%d", len(set(self.baseResult)))
        
        qDistinct = "select distinct(rxcui) from lookup where name like \'%"+cleanQ+"%\'"
        print "distinctQuery:%s" % qDistinct
        self.logger.info("distinctQuery:%s" % qDistinct)
        self.c.execute(qDistinct)
        distinctResult = self.c.fetchall()
        print "numDistinct:%d", len(distinctResult)
        print "set numDistinct:%d", len(set(distinctResult))
        self.logger.info("numDistinct:%d", len(distinctResult))
        self.logger.info("set numDistinct:%d", len(set(distinctResult)))
        
        
    def processParen(self,query):
        """
        using ferrous sulfate example the paren terms are a separate set and have to
        be anded with the original terms. Return list with best match and put on top. 
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
    
    def cleanBaseQuery(self, query):
        """
        """
        return query.lower().strip()
                                      
    def cleanQuery(self,query):
        """
        this will end up becoming list of queries PO->oral, pill, etc...
        """
        print "query before clean punct:%s" % query
        self.logger.info("query before clean punct:%s" % query)
        replaceSpace = re.sub("-"," ",query.lower())
        cleanPunct = re.sub("'", "", replaceSpace)
        print "clean punct:%s" % cleanPunct
        self.logger.info("clean punct:%s" % cleanPunct)
        return cleanPunct
    
    def test(self):
        with open("/Users/dc/TestCode/TestCoding/nomatch.csv") as f:
            for line in f:
                print line
                self.processQuery(line)
    def close(self):
        #self.logger.close()
        print "numBaseResult:%d" % self.numBaseResult
        print "self.zeroBaseResult:%d" % self.zeroBaseResult
        
        
m = Match()
m.test()
m.close()

