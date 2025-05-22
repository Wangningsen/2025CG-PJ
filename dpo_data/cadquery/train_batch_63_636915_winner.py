import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,56))
r=w0.sketch().arc((17,-83),(21,-85),(23,-80)).arc((20,-80),(17,-83)).assemble().finalize().extrude(-113).union(w0.sketch().segment((-28,56),(-28,83)).arc((-95,4),(13,10)).segment((-19,11)).segment((-19,56)).close().assemble().push([(76,-14)]).circle(24).push([(74,1)]).circle(7,mode='s').finalize().extrude(-43))