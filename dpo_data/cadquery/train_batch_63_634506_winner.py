import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,29))
r=w0.sketch().segment((-76,-70),(-56,-100)).segment((-39,-89)).segment((-60,-68)).segment((-42,-48)).close().assemble().push([(-73,19)]).circle(3).push([(34,58)]).circle(42).reset().face(w0.sketch().segment((-2,-24),(3,-30)).segment((19,-42)).segment((3,-65)).segment((37,-44)).segment((18,-13)).close().assemble()).finalize().extrude(-58)