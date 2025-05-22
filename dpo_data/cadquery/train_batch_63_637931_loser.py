import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().push([(-58,27)]).circle(42).circle(11,mode='s').finalize().extrude(-60).union(w0.sketch().segment((8,23),(15,-55)).segment((35,-53)).segment((35,-69)).segment((89,-69)).segment((89,-46)).segment((100,-45)).segment((93,33)).close().assemble().finalize().extrude(-5))