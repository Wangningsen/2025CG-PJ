import cadquery as cq
w0=cq.Workplane('YZ',origin=(-49,0,0))
w1=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((-57,-36),(-49,-100)).segment((57,-87)).segment((51,-39)).arc((15,-49),(-16,-29)).segment((-16,-20)).segment((-28,-22)).segment((-28,-28)).segment((-22,-28)).segment((-22,-34)).close().assemble().finalize().extrude(10).union(w1.workplane(offset=-47/2).moveTo(77,26).cylinder(47,23))