import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,6))
r=w0.workplane(offset=-92/2).moveTo(35.5,76.5).box(57,47,92).union(w0.sketch().segment((-64,-100),(-57,-100)).segment((-44,-69)).segment((-14,-95)).segment((-20,-100)).segment((35,-100)).segment((35,-37)).segment((-64,-37)).close().assemble().push([(27,-81)]).rect(12,4,mode='s').finalize().extrude(79))