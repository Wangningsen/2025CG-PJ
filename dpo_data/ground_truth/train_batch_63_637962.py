import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.workplane(offset=-75/2).moveTo(78.5,0).box(43,128,75).union(w0.sketch().push([(-49,-5.5)]).rect(102,71).push([(-20,-27)]).rect(8,18,mode='s').finalize().extrude(37))