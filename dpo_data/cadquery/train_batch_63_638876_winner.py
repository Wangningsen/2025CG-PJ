import cadquery as cq
w0=cq.Workplane('YZ',origin=(-45,0,0))
w1=cq.Workplane('YZ',origin=(-46,0,0))
r=w0.sketch().segment((-93,-35),(-48,-100)).segment((-11,-74)).segment((-56,-9)).close().assemble().reset().face(w0.sketch().segment((-2,29),(27,-26)).segment((53,-13)).segment((24,43)).close().assemble()).push([(21,28)]).circle(7,mode='s').push([(42,96)]).circle(4).finalize().extrude(46).union(w0.sketch().arc((34,-9),(45,9),(34,26)).close().assemble().finalize().extrude(91)).union(w1.sketch().segment((74,87),(74,88)).arc((83,79),(93,87)).close().assemble().finalize().extrude(85))