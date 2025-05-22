import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.workplane(offset=-148/2).box(8,84,148).union(w0.sketch().circle(24).push([(-5,16.5)]).rect(10,5,mode='s').finalize().extrude(52))