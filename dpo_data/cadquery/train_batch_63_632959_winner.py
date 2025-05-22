import cadquery as cq
w0=cq.Workplane('YZ',origin=(-60,0,0))
w1=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().push([(-80,67)]).circle(20).push([(-67,55)]).circle(2,mode='s').finalize().extrude(45).union(w1.sketch().push([(22,62)]).circle(38).circle(37,mode='s').finalize().extrude(-48))