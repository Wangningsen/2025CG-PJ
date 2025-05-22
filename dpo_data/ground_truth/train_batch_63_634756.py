import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().arc((-48,-14),(-100,-40),(-45,-57)).segment((-22,-57)).arc((0,-66),(22,-57)).segment((48,-57)).segment((48,-26)).arc((82,59),(8,3)).arc((-8,3),(-22,-4)).segment((-48,-4)).close().assemble().push([(52,21)]).circle(8,mode='s').finalize().extrude(-72).union(w0.sketch().arc((-48,-12),(-45,-24),(-37,-33)).arc((64,28),(-48,-12)).assemble().finalize().extrude(61)).union(w1.sketch().segment((1,-64),(38,-64)).arc((20,-50),(1,-64)).assemble().finalize().extrude(64))