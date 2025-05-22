import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,4))
r=w0.sketch().circle(100).push([(10.5,25)]).rect(67,80,mode='s').finalize().extrude(-8)