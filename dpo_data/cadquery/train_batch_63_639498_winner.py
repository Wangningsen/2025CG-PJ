import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.sketch().segment((-89,-28),(79,-52)).segment((89,33)).segment((-78,53)).close().assemble().push([(1,1)]).rect(46,34,mode='s').finalize().extrude(-119).union(w0.workplane(offset=81/2).cylinder(81,74))