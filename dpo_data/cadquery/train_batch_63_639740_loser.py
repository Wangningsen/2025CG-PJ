import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().segment((-100,-65),(-2,-65)).arc((-1,-63),(0,-65)).segment((4,-65)).segment((4,-61)).segment((-100,-61)).close().assemble().finalize().extrude(-84).union(w0.sketch().push([(39,4)]).circle(61).circle(37,mode='s').finalize().extrude(-37))