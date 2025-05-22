import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=-75/2).moveTo(16,54).cylinder(75,46).union(w0.sketch().segment((-44,-87),(-18,-87)).segment((-18,-72)).arc((-15,-64),(-18,-55)).segment((-18,-40)).segment((-44,-40)).segment((-44,-55)).arc((-46,-64),(-44,-72)).close().assemble().finalize().extrude(42)).union(w0.sketch().push([(27,-67)]).circle(33).push([(26.5,-67.5)]).rect(33,43,mode='s').finalize().extrude(57)).union(w1.sketch().push([(3.5,-31)]).rect(63,62).push([(3,-31)]).rect(24,6,mode='s').finalize().extrude(57))