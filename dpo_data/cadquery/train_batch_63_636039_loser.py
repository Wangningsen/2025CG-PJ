import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().push([(0,44)]).circle(56).push([(-1,7)]).rect(42,10,mode='s').push([(-1,79.5)]).rect(42,5,mode='s').finalize().extrude(-40).union(w0.sketch().push([(9,-70.5)]).rect(48,59).push([(9,-70)]).rect(46,32,mode='s').finalize().extrude(40))