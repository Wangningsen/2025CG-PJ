import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
w1=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().circle(47).push([(38,-23)]).circle(4,mode='s').finalize().extrude(-34).union(w1.workplane(offset=-81/2).cylinder(81,100))