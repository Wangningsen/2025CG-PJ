import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
w1=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().push([(0,77.5)]).rect(140,45).push([(-52,82)]).circle(16,mode='s').push([(0,77.5)]).rect(18,39,mode='s').finalize().extrude(29).union(w1.workplane(offset=79/2).moveTo(-51,0).cylinder(79,49))