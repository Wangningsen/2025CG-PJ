import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().push([(-25.5,54.5)]).rect(97,91).reset().face(w0.sketch().segment((-45,52),(-28,39)).segment((-6,56)).segment((-25,72)).close().assemble(),mode='s').push([(50,-76.5)]).rect(48,47).finalize().extrude(84)