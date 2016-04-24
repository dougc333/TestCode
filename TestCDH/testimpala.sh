#!/bin/bash -p

ssh r2341-d5-us02 "impala-shell -q 'select * from default.testme;'"
