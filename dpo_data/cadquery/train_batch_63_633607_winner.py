import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.workplane(offset=-31/2).moveTo(-66,-35).cylinder(31,34).union(w0.sketch().push([(61,30)]).circle(39).circle(6,mode='s').finalize().extrude(79)).union(w1.sketch().segment((-14,-31),(-14,-28)).segment((-3,-28)).segment((-3,-32)).segment((-11,-32)).arc((-7,-36),(-3,-38)).segment((-3,-71)).segment((-1,-71)).segment((-1,-38)).arc((16,-32),(22,-15)).arc((21,-11),(19,-8)).arc((-11,-1),(-14,-31)).assemble().finalize().extrude(56))