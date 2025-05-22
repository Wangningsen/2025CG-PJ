import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.workplane(offset=71/2).moveTo(70.5,-26).box(59,104,71).union(w0.sketch().arc((-28,41),(-88,-36),(-7,19)).arc((33,67),(-28,41)).assemble().reset().face(w0.sketch().segment((-6,31),(7,23)).segment((25,55)).segment((13,62)).close().assemble(),mode='s').finalize().extrude(84))