import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().circle(15).reset().face(w0.sketch().segment((-11,-9),(8,-12)).segment((11,9)).segment((-8,12)).close().assemble(),mode='s').finalize().extrude(-92).union(w0.sketch().segment((-36,46),(-36,65)).arc((32,-67),(-27,69)).segment((-4,69)).segment((-4,46)).close().assemble().finalize().extrude(108))