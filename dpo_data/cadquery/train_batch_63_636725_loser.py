import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().circle(100).push([(44.5,-46)]).rect(31,20,mode='s').finalize().extrude(-130)