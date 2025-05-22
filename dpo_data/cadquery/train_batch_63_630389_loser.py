import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-79))
r=w0.sketch().segment((-91,-55),(28,-100)).segment((37,-75)).arc((89,-12),(73,64)).segment((74,52)).segment((-36,-59)).segment((-79,-21)).segment((25,97)).arc((-69,68),(-83,-28)).close().assemble().finalize().extrude(158)