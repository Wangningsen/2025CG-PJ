import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.workplane(offset=-98/2).moveTo(-15,43).cylinder(98,22).union(w0.sketch().arc((30,-65),(33,-63),(36,-62)).segment((36,-43)).arc((37,-38),(36,-35)).segment((36,-17)).arc((31,-11),(36,-6)).segment((36,6)).segment((30,6)).segment((30,-35)).arc((29,-38),(30,-43)).close().assemble().finalize().extrude(102))