import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().segment((-38,-100),(-10,-100)).segment((1,-100)).segment((53,-100)).segment((53,-17)).segment((25,-17)).segment((25,-16)).segment((1,-16)).segment((1,-17)).segment((-38,-17)).close().assemble().reset().face(w0.sketch().segment((-17,-93),(7,-100)).segment((31,-19)).segment((8,-13)).close().assemble(),mode='s').finalize().extrude(-58).union(w0.workplane(offset=19/2).moveTo(-3,42).cylinder(19,50)).union(w1.workplane(offset=-67/2).moveTo(15,-12).cylinder(67,14))