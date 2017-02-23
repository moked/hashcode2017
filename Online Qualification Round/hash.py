import math
import re
import numpy as np
import operator

f = open("example.in")
fw = open("1example.txt", 'w+')

V = 0   # number of vidoes
E = 0   # number of endpoints
R = 0   # number of requests
C = 0   # number of cache servers
X = 0   # capacity of each cache server

videoSizes = []
endpoints = []
requests = []

outputs = []

first_line = f.readline()
numbers = first_line.split()

V = int(numbers[0])
E = int(numbers[1])
R = int(numbers[2])
C = int(numbers[3])
X = int(numbers[4])

serversCapacities = np.zeros(C)

second_line = f.readline()
videoSizesArr = second_line.split()

for x in xrange(0, len(videoSizesArr)):
    videoSizes.append(int(videoSizesArr[x]))
    pass

class Endpoint:
    def __init__(self, id, dl, noCacheServers, cacheLatencies):
        self.id = id
        self.dl = dl
        self.noCacheServers = noCacheServers
        self.cacheLatencies = cacheLatencies

class CacheLatency:
    def __init__(self, id, latency):
        self.id = id
        self.latency = latency

class Request:
    def __init__(self, vid, eid, noRequestsm, videoSize):
        self.vid = vid
        self.eid = eid
        self.noRequests = noRequests
        self.videoSize = videoSize

class Output:
    def __init__(self, sid, videoArr):
        self.sid = sid
        self.videoArr = videoArr

def checkServerCapacity(sid, videoSize):
    if serversCapacities[sid] + videoSize > X:
        return False
    else:
        serversCapacities[sid] += videoSize
        return True

def addToOutput(sid, vid):

    for x in xrange(0, len(outputs)):
        if outputs[x].sid == sid:
            for y in xrange(0, len(outputs[x].videoArr)):
                if outputs[x].videoArr[y] == vid:
                    vidFound = True 
                    return # vidoe already in this cache server

            outputs[x].videoArr.append(vid)
            return
    
    vidArr = [vid]
    output = Output(sid, vidArr)
    outputs.append(output)

for x in xrange(0, E):
    endpointId = x
    line = f.readline().split()
    dl = int(line[0])
    noCacheServers = int(line[1])
    cacheLatencies = []

    for y in xrange(0, noCacheServers):
        line = f.readline().split()
        serverId = int(line[0])
        serverLatency = int(line[1])

        cacheLatency = CacheLatency(serverId, serverLatency)
        cacheLatencies.append(cacheLatency)

    cacheLatencies.sort(key = operator.attrgetter('latency'))

    endpoint = Endpoint(endpointId, dl, noCacheServers, cacheLatencies)
    endpoints.append(endpoint)

for x in xrange(0, R):
    line = f.readline().split()
    vid = int(line[0])
    eid = int(line[1])
    noRequests = int(line[2])
    videoSize = videoSizes[vid]
    r = Request(vid, eid, noRequests, videoSize)
    requests.append(r)

requests.sort(key = operator.attrgetter('videoSize'), reverse=False)

for x in xrange(0, R):
    request = requests[x]

    for y in xrange(0, endpoints[request.eid].noCacheServers):

        if checkServerCapacity(endpoints[request.eid].cacheLatencies[y].id, request.videoSize):
            addToOutput(endpoints[request.eid].cacheLatencies[y].id, request.vid)
            break

fw.write(str(len(outputs)))
fw.write('\n')
for x in xrange(0, len(outputs)):

    fw.write(str(outputs[x].sid))
    fw.write(' ')

    for y in xrange(0, len(outputs[x].videoArr)):
        fw.write(str(outputs[x].videoArr[y]))
        fw.write(' ')

    fw.write('\n')
    pass

f.close()
fw.close()