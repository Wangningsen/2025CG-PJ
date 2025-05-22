import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
w1=cq.Workplane('YZ',origin=(67,0,0))
r=w0.sketch().segment((-89,75),(-85,72)).arc((-73,31),(-32,26)).segment((-28,24)).segment((-27,26)).arc((-15,39),(-9,56)).segment((-8,58)).segment((-12,60)).arc((-24,92),(-59,98)).segment((-63,100)).segment((-64,100)).arc((-79,96),(-89,85)).segment((-85,85)).segment((-85,75)).close().assemble().finalize().extrude(-93).union(w1.workplane(offset=-91/2).moveTo(15,-27).cylinder(91,73))