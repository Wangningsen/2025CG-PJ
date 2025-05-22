import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((78,-100),(87,-100)).segment((87,-69)).arc((91,-63),(87,-56)).segment((87,-26)).segment((78,-26)).segment((78,-56)).arc((75,-63),(78,-69)).close().assemble().finalize().extrude(-64).union(w0.workplane(offset=115/2).moveTo(16,-41).cylinder(115,28)).union(w1.sketch().arc((-49,-53),(-37,-90),(-36,-51)).arc((-43,-53),(-49,-53)).assemble().finalize().extrude(-144))