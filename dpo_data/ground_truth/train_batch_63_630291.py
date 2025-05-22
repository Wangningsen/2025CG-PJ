import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
w1=cq.Workplane('XY',origin=(0,0,-52))
r=w0.workplane(offset=37/2).moveTo(-38,61).cylinder(37,39).union(w0.workplane(offset=70/2).moveTo(31.5,-62).box(91,76,70)).union(w0.workplane(offset=72/2).moveTo(23,-27).cylinder(72,25)).union(w1.sketch().segment((-55,-26),(-21,-26)).segment((-21,-32)).segment((16,-32)).arc((23,-37),(31,-32)).segment((68,-32)).segment((68,-22)).segment((32,-22)).segment((32,-19)).segment((27,-19)).arc((23,-18),(19,-19)).segment((-55,-19)).close().assemble().finalize().extrude(57))