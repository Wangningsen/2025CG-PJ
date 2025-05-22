import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.sketch().segment((-100,46),(-99,46)).segment((-99,38)).segment((-47,38)).segment((-47,-4)).segment((10,-4)).segment((10,86)).segment((-47,86)).segment((-47,60)).segment((-99,60)).segment((-99,52)).segment((-100,52)).close().assemble().push([(-55,49)]).rect(16,4,mode='s').finalize().extrude(-53).union(w0.workplane(offset=-14/2).moveTo(-10,-53).cylinder(14,3)).union(w1.sketch().segment((63,-86),(100,-86)).segment((100,-74)).arc((81,-81),(63,-74)).close().assemble().finalize().extrude(77))