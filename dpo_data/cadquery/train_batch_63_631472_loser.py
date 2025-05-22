import cadquery as cq
w0=cq.Workplane('YZ',origin=(-11,0,0))
r=w0.workplane(offset=-39/2).moveTo(54,28).cylinder(39,12).union(w0.sketch().arc((-36,-27),(-54,-90),(11,-66)).segment((39,-66)).segment((39,-8)).segment((-36,-8)).close().assemble().push([(3.5,-47)]).rect(11,18,mode='s').finalize().extrude(11)).union(w0.workplane(offset=61/2).moveTo(4,61.5).box(70,77,61))