import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().segment((-68,-51),(-57,-60)).arc((-43,-82),(-18,-91)).segment((-7,-100)).segment((4,-84)).arc((13,-76),(20,-65)).segment((33,-50)).segment((22,-41)).arc((8,-18),(-16,-9)).segment((-27,0)).segment((-40,-16)).arc((-49,-24),(-55,-35)).close().assemble().push([(12,44)]).circle(56).finalize().extrude(-130)