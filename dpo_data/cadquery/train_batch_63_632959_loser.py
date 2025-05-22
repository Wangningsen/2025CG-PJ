import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().push([(-79,67)]).circle(21).push([(-69,54)]).circle(2,mode='s').finalize().extrude(-45).union(w1.sketch().push([(22,62)]).circle(38).circle(37,mode='s').finalize().extrude(-48))