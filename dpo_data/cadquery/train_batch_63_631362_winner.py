import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.workplane(offset=12/2).moveTo(57,-69).cylinder(12,31).union(w0.sketch().segment((-66,19),(-25,-23)).segment((32,29)).segment((2,62)).close().assemble().push([(-17,22)]).circle(27,mode='s').finalize().extrude(68)).union(w0.sketch().arc((-83,39),(-56,37),(-33,19)).arc((-33,98),(-83,39)).assemble().finalize().extrude(81))