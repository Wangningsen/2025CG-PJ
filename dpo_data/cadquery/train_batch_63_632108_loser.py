import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().segment((-53,-100),(30,-100)).segment((8,-40)).segment((11,-39)).segment((29,-29)).segment((-53,-29)).close().assemble().finalize().extrude(-31).union(w0.workplane(offset=47/2).moveTo(12,59).cylinder(47,41))