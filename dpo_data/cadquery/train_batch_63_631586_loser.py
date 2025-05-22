import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('YZ',origin=(-19,0,0))
r=w0.sketch().segment((-7,-45),(21,-45)).arc((50,-100),(80,-45)).segment((81,-45)).segment((81,66)).segment((-7,66)).close().assemble().finalize().extrude(-101).union(w0.sketch().arc((-36,90),(-75,21),(-1,52)).arc((-24,69),(-36,90)).assemble().push([(-44.5,48.5)]).rect(23,79,mode='s').finalize().extrude(-51)).union(w1.workplane(offset=44/2).moveTo(49,31).cylinder(44,51))