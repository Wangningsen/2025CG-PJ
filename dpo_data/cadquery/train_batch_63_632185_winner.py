import cadquery as cq
w0=cq.Workplane('YZ',origin=(-91,0,0))
r=w0.sketch().arc((-53,-62),(39,-82),(4,7)).arc((7,-49),(-53,-62)).assemble().finalize().extrude(54).union(w0.workplane(offset=183/2).moveTo(42.5,12).box(21,176,183))