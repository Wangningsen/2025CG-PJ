import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-89))
r=w0.workplane(offset=-11/2).box(22,4,11).union(w0.sketch().rect(104,52).rect(10,10,mode='s').finalize().extrude(189))