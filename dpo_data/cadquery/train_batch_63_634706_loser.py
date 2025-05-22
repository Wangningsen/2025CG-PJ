import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().arc((-89,-15),(-60,-52),(-74,-88)).segment((67,-88)).segment((67,50)).segment((74,75)).segment((-37,100)).segment((-46,54)).segment((-89,54)).segment((-89,42)).segment((-56,42)).segment((-56,-12)).segment((-89,-12)).close().assemble().finalize().extrude(-88).union(w1.sketch().arc((68,-31),(84,-68),(81,-100)).arc((88,-66),(68,-31)).assemble().finalize().extrude(-122))