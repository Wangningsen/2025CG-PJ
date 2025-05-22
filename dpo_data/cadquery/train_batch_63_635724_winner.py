import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,66,0))
w1=cq.Workplane('XY',origin=(0,0,-6))
r=w0.workplane(offset=-136/2).moveTo(23,0).box(154,128,136).union(w1.sketch().push([(0,55.5)]).rect(166,29).push([(-39,55)]).circle(7,mode='s').finalize().extrude(-94))