import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-64,-46),(-64,-19)).segment((-46,-19)).arc((-100,-38),(-62,-69)).segment((-62,-81)).segment((22,-81)).segment((22,-94)).segment((61,-94)).segment((61,-46)).close().assemble().finalize().extrude(-97).union(w1.workplane(offset=101/2).moveTo(43,83).cylinder(101,17))