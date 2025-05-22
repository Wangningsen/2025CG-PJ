import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.workplane(offset=-98/2).moveTo(-15,43).cylinder(98,22).union(w0.sketch().segment((30,-65),(32,-65)).arc((33,-63),(35,-62)).segment((35,-60)).arc((37,-39),(31,-18)).segment((31,-10)).segment((36,-10)).segment((36,6)).segment((30,6)).segment((30,-42)).arc((29,-43),(30,-44)).close().assemble().finalize().extrude(102))