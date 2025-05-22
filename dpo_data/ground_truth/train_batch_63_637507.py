import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().segment((80,-100),(95,-100)).segment((95,-43)).arc((93,-42),(95,-40)).segment((95,10)).segment((80,10)).close().assemble().push([(89,-10)]).circle(3,mode='s').finalize().extrude(-101).union(w0.sketch().segment((0,-85),(81,-85)).segment((81,-54)).arc((96,-16),(81,22)).segment((81,52)).segment((0,52)).segment((0,22)).arc((-15,-16),(0,-54)).close().assemble().push([(3,23)]).circle(2,mode='s').finalize().extrude(-71)).union(w1.workplane(offset=118/2).moveTo(41,-94).box(64,4,118))