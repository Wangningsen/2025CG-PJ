import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
w1=cq.Workplane('XY',origin=(0,0,18))
r=w0.sketch().push([(-29,-11)]).circle(23).reset().face(w0.sketch().segment((-34,-23),(-33,-23)).arc((-28,-26),(-23,-23)).segment((-22,-23)).segment((-22,-21)).segment((-23,-21)).arc((-28,-18),(-33,-21)).segment((-34,-21)).close().assemble(),mode='s').finalize().extrude(76).union(w1.sketch().segment((12,-100),(34,-100)).segment((34,-92)).arc((23,-93),(12,-92)).close().assemble().finalize().extrude(34))