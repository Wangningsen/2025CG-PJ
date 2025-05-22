import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
w1=cq.Workplane('YZ',origin=(-20,0,0))
r=w0.workplane(offset=-69/2).moveTo(-8,-8).cylinder(69,17).union(w0.workplane(offset=42/2).moveTo(-8,-8).cylinder(42,51)).union(w1.sketch().segment((-58,-26),(-44,-46)).segment((-31,-39)).segment((-31,-32)).segment((-19,-32)).segment((-19,-35)).segment((-17,-32)).arc((-8,-33),(1,-31)).arc((53,36),(-33,16)).arc((-32,-4),(-47,-18)).close().assemble().finalize().extrude(120))