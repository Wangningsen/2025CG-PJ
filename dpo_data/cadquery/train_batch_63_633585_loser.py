import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.sketch().push([(-25.5,54.5)]).rect(97,91).reset().face(w0.sketch().segment((-44,52),(-24,38)).segment((-7,55)).segment((-27,70)).close().assemble(),mode='s').push([(50,-76.5)]).rect(48,47).finalize().extrude(-84)