import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
w1=cq.Workplane('YZ',origin=(-90,0,0))
r=w0.workplane(offset=-55/2).cylinder(55,100).union(w1.sketch().push([(36,-75)]).circle(16).push([(36.5,-75)]).rect(21,14,mode='s').finalize().extrude(181))