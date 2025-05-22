import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.workplane(offset=-44/2).moveTo(-55,-57).cylinder(44,25).union(w0.sketch().push([(2,4)]).circle(78).circle(39,mode='s').finalize().extrude(156))