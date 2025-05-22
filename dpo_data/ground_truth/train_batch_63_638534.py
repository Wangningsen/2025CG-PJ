import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
w1=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().segment((19,-48),(61,-60)).segment((78,1)).segment((67,4)).segment((67,-11)).segment((65,-11)).segment((65,5)).segment((37,13)).close().assemble().finalize().extrude(17).union(w0.sketch().arc((-80,65),(-78,74),(-75,84)).arc((-88,77),(-80,65)).assemble().reset().face(w0.sketch().segment((9,-84),(88,-84)).segment((88,37)).segment((69,37)).arc((48,0),(9,-19)).close().assemble()).finalize().extrude(142)).union(w1.workplane(offset=-41/2).moveTo(49,-23.5).box(68,91,41))