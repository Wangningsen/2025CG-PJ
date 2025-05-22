import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.workplane(offset=-31/2).moveTo(-66,-35).cylinder(31,34).union(w0.sketch().push([(61,30)]).circle(39).circle(6,mode='s').finalize().extrude(79)).union(w1.sketch().segment((-12,-33),(-12,-28)).segment((-1,-28)).segment((-1,-36)).segment((-8,-36)).arc((-6,-37),(-3,-38)).segment((-3,-71)).segment((-1,-71)).segment((-1,-38)).arc((10,2),(-12,-33)).assemble().finalize().extrude(56))