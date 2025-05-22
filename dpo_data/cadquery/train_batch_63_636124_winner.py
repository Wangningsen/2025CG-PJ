import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
w1=cq.Workplane('XY',origin=(0,0,-85))
r=w0.sketch().push([(8,14)]).circle(20).push([(-1,17)]).circle(10,mode='s').finalize().extrude(-20).union(w1.sketch().push([(0,-18)]).rect(200,20).push([(42.5,-24)]).rect(3,4,mode='s').finalize().extrude(171))