import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.sketch().arc((-67,37),(54,-39),(-35,72)).segment((-35,74)).segment((-38,61)).segment((-67,68)).close().assemble().finalize().extrude(-60).union(w0.workplane(offset=140/2).moveTo(-27,-70).cylinder(140,11))