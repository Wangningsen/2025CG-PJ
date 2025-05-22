import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().circle(100).push([(-22,-89)]).rect(14,10,mode='s').push([(-1.5,80.5)]).rect(7,7,mode='s').finalize().extrude(-192)