import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().arc((-89,-13),(-61,-46),(-74,-88)).segment((67,-88)).segment((67,48)).segment((74,77)).segment((-37,100)).segment((-47,54)).segment((-89,54)).segment((-89,42)).segment((-56,42)).segment((-56,-12)).segment((-89,-12)).close().assemble().finalize().extrude(-88).union(w1.sketch().arc((67,-30),(82,-63),(81,-100)).arc((88,-62),(67,-30)).assemble().finalize().extrude(-122))