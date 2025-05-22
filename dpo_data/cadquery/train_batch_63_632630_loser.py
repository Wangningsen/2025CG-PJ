import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('XY',origin=(0,0,-45))
r=w0.workplane(offset=-75/2).moveTo(16,54).cylinder(75,46).union(w0.sketch().segment((-46,-87),(-18,-87)).segment((-18,-71)).arc((-21,-45),(-44,-52)).segment((-46,-52)).close().assemble().push([(-22.5,-76.5)]).rect(11,11,mode='s').finalize().extrude(42)).union(w0.sketch().push([(27,-67)]).circle(33).push([(26.5,-67.5)]).rect(33,43,mode='s').finalize().extrude(57)).union(w1.sketch().push([(3.5,-31)]).rect(63,62).push([(3,-31)]).rect(24,6,mode='s').finalize().extrude(57))