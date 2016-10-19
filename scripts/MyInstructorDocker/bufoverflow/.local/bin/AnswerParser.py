#!/usr/bin/env python

# AnswerParser.py
# Description: * Read answer.config
#              * Parse stdin and stdout files based on answer.config
#              * Create a json file

import json
import glob
import os
import sys

UBUNTUHOME = "/home/ubuntu/"
exec_proglist = []
stdinfnameslist = []
stdoutfnameslist = []
timestamplist = []
nametags = {}

def ParseAnswer():
    configfilename = '%s/.local/config/%s' % (UBUNTUHOME, "answer.config")
    configfile = open(configfilename)
    configfilelines = configfile.readlines()
    configfile.close()
  
    for line in configfilelines:
        linestrip = line.rstrip()
        if linestrip:
            if not linestrip.startswith('#'):
                #print "Current linestrip is (%s)" % linestrip
                (each_key, each_value) = linestrip.split('=', 1)
                each_key = each_key.strip()
                if not each_key.isalnum():
                    sys.stderr.write("ERROR: answer.config contains key (%s) not alphanumeric\n" % each_key)
                    sys.exit(1)
                if each_key in nametags:
                    nametags[each_key].append(each_value)
                else:
                    nametags[each_key] = []
                    nametags[each_key].append(each_value)
        #else:
        #    print "Skipping empty linestrip is (%s)" % linestrip

    outputjsonfname = '%s/.local/config/%s' % (UBUNTUHOME, "answer.json")
    #print "Outputjsonfname is (%s)" % outputjsonfname
        
    #print nametags
    jsonoutput = open(outputjsonfname, "w")
    jsondumpsoutput = json.dumps(nametags, indent=4)
    jsonoutput.write(jsondumpsoutput)
    jsonoutput.write('\n')
    jsonoutput.close()

# Usage: AnswerParser.py
# Arguments:
#     None
def main():
    #print "Running AnswerParser.py"
    if len(sys.argv) != 1:
        sys.stderr.write("Usage: AnswerParser.py\n")
        sys.exit(1)

    ParseAnswer()
    return 0

if __name__ == '__main__':
    sys.exit(main())

