#!/bin/bash  
gcov example2 -r
mv example2.cpp.gcov ../example110.cpp.gcov
gcov example2 -r
mv example2.cpp.gcov ../example111.cpp.gcov
gcov example2 -r
mv example2.cpp.gcov ../example112.cpp.gcov
gcov example2 -r
mv example2.cpp.gcov ../example113.cpp.gcov