import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().push([(-55,32)]).circle(45).reset().face(w0.sketch().segment((50,-62),(54,-62)).segment((54,-13)).arc((52,-12),(54,-12)).segment((54,3)).segment((50,3)).close().assemble()).finalize().extrude(-43).union(w0.workplane(offset=1/2).moveTo(52,-29).cylinder(1,48))