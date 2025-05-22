import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().push([(-58,27)]).circle(42).circle(11,mode='s').circle(2).finalize().extrude(-60).union(w0.sketch().segment((8,25),(15,-53)).segment((35,-51)).segment((35,-69)).segment((89,-69)).segment((89,-46)).segment((100,-45)).segment((92,33)).close().assemble().finalize().extrude(-5))