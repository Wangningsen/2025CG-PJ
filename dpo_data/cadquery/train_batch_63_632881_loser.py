import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,18))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.workplane(offset=-59/2).moveTo(-11.5,33).box(19,18,59).union(w0.sketch().segment((-11,-16),(35,-16)).segment((35,14)).arc((41,33),(35,52)).segment((35,55)).segment((33,55)).arc((-30,60),(-11,-2)).close().assemble().finalize().extrude(5)).union(w0.workplane(offset=22/2).moveTo(-38,90).box(30,20,22)).union(w1.workplane(offset=-31/2).moveTo(27,-74).cylinder(31,26))