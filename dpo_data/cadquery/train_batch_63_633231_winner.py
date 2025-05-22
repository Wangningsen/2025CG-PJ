import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-77))
r=w0.sketch().push([(-27,81)]).circle(19).circle(15,mode='s').finalize().extrude(54).union(w0.sketch().push([(0,-18)]).circle(82).push([(0,-17)]).rect(28,88,mode='s').finalize().extrude(153))