import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,37))
w1=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().segment((-100,-49),(-76,-49)).segment((-76,-62)).segment((-58,-62)).segment((-58,-49)).segment((-35,-49)).segment((-35,9)).segment((-58,9)).segment((-58,22)).segment((-76,22)).segment((-76,9)).segment((-100,9)).close().assemble().push([(-67,-21)]).circle(4,mode='s').finalize().extrude(-79).union(w0.sketch().arc((34,4),(92,-3),(84,43)).arc((79,4),(34,4)).assemble().finalize().extrude(-62)).union(w1.workplane(offset=-36/2).moveTo(16.5,43).box(3,38,36))