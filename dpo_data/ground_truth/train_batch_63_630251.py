import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
r=w0.sketch().circle(100).push([(-86,27)]).rect(8,26,mode='s').push([(-6,-66.5)]).rect(56,23,mode='s').finalize().extrude(-14)