import cadquery as cq
w0=cq.Workplane('YZ',origin=(-91,0,0))
r=w0.sketch().arc((-53,-61),(40,-81),(4,8)).arc((5,-52),(-53,-61)).assemble().finalize().extrude(55).union(w0.workplane(offset=183/2).moveTo(42.5,12).box(21,176,183))