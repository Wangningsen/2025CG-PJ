import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,61))
r=w0.sketch().push([(-77,17)]).circle(23).push([(52,0)]).circle(48).reset().face(w0.sketch().segment((28,-13),(33,-13)).arc((58,-30),(82,-13)).segment((88,-13)).segment((88,-7)).segment((80,-7)).arc((58,10),(36,-7)).segment((28,-7)).close().assemble(),mode='s').finalize().extrude(-122)