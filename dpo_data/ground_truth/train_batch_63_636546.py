import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().push([(79,62)]).circle(21).push([(83,73)]).circle(3,mode='s').finalize().extrude(-73).union(w0.sketch().segment((68,-83),(76,-83)).segment((76,-41)).segment((68,-41)).segment((68,-69)).arc((71,-74),(68,-80)).close().assemble().finalize().extrude(-56)).union(w0.workplane(offset=88/2).moveTo(-56,-15).box(88,8,88))