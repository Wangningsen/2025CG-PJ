import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('ZX',origin=(0,-39,0))
r=w0.sketch().segment((-75,-66),(-66,-66)).arc((-38,-73),(-11,-66)).segment((-10,-66)).segment((-10,-65)).arc((2,-46),(4,-22)).arc((-16,99),(-72,-7)).arc((-74,-9),(-75,-11)).segment((-75,-12)).arc((-81,-33),(-75,-52)).close().assemble().finalize().extrude(-104).union(w1.workplane(offset=129/2).moveTo(-64,31).cylinder(129,36))