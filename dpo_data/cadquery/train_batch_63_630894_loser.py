import cadquery as cq
w0=cq.Workplane('YZ',origin=(-87,0,0))
w1=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().segment((-55,51),(23,51)).segment((23,90)).segment((-46,60)).segment((-55,79)).close().assemble().reset().face(w0.sketch().segment((-55,89),(22,96)).segment((23,93)).segment((23,100)).segment((-55,100)).close().assemble()).finalize().extrude(11).union(w1.workplane(offset=-157/2).moveTo(11.5,36.5).box(151,37,157))