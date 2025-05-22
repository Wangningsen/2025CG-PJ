import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,70,0))
r=w0.sketch().segment((-1,-17),(63,-100)).segment((81,-87)).segment((16,-4)).close().assemble().finalize().extrude(-140).union(w0.sketch().segment((-81,99),(-32,-13)).segment((-28,-12)).segment((-78,100)).close().assemble().finalize().extrude(-83))