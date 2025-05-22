import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,69))
r=w0.sketch().arc((-76,-95),(-60,-97),(-64,-83)).arc((-78,-80),(-76,-95)).assemble().finalize().extrude(-138).union(w0.sketch().arc((-7,-20),(69,-37),(49,38)).arc((-53,83),(-7,-20)).assemble().reset().face(w0.sketch().arc((19,-13),(50,-17),(40,12)).arc((31,-2),(19,-13)).assemble(),mode='s').finalize().extrude(-62))