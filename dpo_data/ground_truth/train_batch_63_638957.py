import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
w1=cq.Workplane('YZ',origin=(-51,0,0))
r=w0.sketch().arc((-15,42),(-99,-16),(-3,-50)).arc((99,10),(-15,42)).assemble().finalize().extrude(116).union(w1.sketch().push([(64,-5.5)]).rect(46,121).push([(64,-6)]).circle(11,mode='s').finalize().extrude(61))