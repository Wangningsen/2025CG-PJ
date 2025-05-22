import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,38,0))
r=w0.sketch().push([(-83,-38)]).circle(17).reset().face(w0.sketch().segment((-93,-42),(-88,-50)).segment((-69,-42)).segment((-74,-34)).close().assemble(),mode='s').finalize().extrude(-118).union(w0.workplane(offset=3/2).moveTo(38.5,-66).box(123,34,3)).union(w0.workplane(offset=41/2).moveTo(-42.5,64.5).box(31,37,41))