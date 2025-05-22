import cadquery as cq
w0=cq.Workplane('YZ',origin=(-91,0,0))
r=w0.sketch().arc((-53,-61),(43,-77),(-1,8)).arc((11,-43),(-36,-67)).segment((-36,-70)).segment((-41,-70)).segment((-41,-66)).arc((-47,-64),(-53,-61)).assemble().finalize().extrude(54).union(w0.workplane(offset=183/2).moveTo(42.5,12).box(21,176,183))