#!/bin/bash

for x in snappy leveldb gflags glog szip lmdb; do brew uninstall $x; brew install --build-from-source -vd $x; done

