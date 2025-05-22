import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.workplane(offset=-45/2).moveTo(-99,-48.5).box(2,103,45).union(w0.sketch().segment((-91,13),(-44,13)).segment((-44,-37)).segment((-42,-37)).segment((-42,13)).segment((-18,13)).segment((-18,61)).segment((-42,61)).segment((-42,100)).segment((-44,100)).segment((-44,61)).segment((-91,61)).close().assemble().finalize().extrude(57)).union(w1.workplane(offset=4/2).moveTo(86,-30).cylinder(4,14))