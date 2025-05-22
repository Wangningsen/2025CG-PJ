import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().circle(100).push([(-19.5,-66)]).rect(29,24,mode='s').finalize().extrude(14)