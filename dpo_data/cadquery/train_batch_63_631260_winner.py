import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().circle(100).push([(-28,-88.5)]).rect(28,9,mode='s').push([(-2,79)]).circle(5,mode='s').finalize().extrude(-192)