import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,69))
r=w0.sketch().segment((-100,5),(-44,-44)).segment((-15,-12)).segment((-71,38)).close().assemble().push([(-57,-4)]).circle(6,mode='s').finalize().extrude(-138).union(w0.workplane(offset=-70/2).moveTo(30.5,0).box(139,144,70))