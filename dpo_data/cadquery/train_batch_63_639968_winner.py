import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=-108/2).moveTo(-41,11).cylinder(108,59).union(w0.workplane(offset=-73/2).moveTo(5,39).cylinder(73,19)).union(w0.sketch().push([(60,-31)]).circle(40).push([(60,-30.5)]).rect(2,65,mode='s').finalize().extrude(-3))