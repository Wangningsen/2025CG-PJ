import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
r=w0.sketch().segment((17,61),(17,98)).arc((-100,-5),(27,-96)).segment((26,-96)).segment((26,-92)).segment((27,-92)).segment((27,-91)).segment((33,-89)).segment((34,-92)).segment((36,-92)).segment((36,-93)).arc((97,-26),(78,61)).close().assemble().push([(0,-0.5)]).rect(46,115,mode='s').finalize().extrude(-115)