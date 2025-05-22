import cadquery as cq
w0=cq.Workplane('YZ',origin=(-77,0,0))
w1=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().arc((-14,-47),(11,-65),(3,-35)).arc((-74,57),(-14,-47)).assemble().push([(-95,12)]).circle(2,mode='s').finalize().extrude(8).union(w0.workplane(offset=89/2).moveTo(-40,8).cylinder(89,4)).union(w1.workplane(offset=55/2).moveTo(71,94).cylinder(55,6))