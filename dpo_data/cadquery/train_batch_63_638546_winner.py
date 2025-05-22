import cadquery as cq
w0=cq.Workplane('YZ',origin=(25,0,0))
w1=cq.Workplane('XY',origin=(0,0,18))
r=w0.sketch().arc((-17,-12),(-50,-77),(12,-39)).arc((-12,-32),(-17,-12)).assemble().reset().face(w0.sketch().arc((11,72),(-26,18),(31,-12)).arc((86,57),(11,72)).assemble()).finalize().extrude(2).union(w0.sketch().segment((-8,15),(-7,15)).arc((-7,16),(-8,18)).close().assemble().reset().face(w0.sketch().segment((35,15),(37,15)).segment((37,18)).arc((36,16),(35,15)).assemble()).finalize().extrude(75)).union(w1.workplane(offset=10/2).moveTo(-60,-49).cylinder(10,40))