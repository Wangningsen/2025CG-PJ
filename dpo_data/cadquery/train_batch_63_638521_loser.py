import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('YZ',origin=(50,0,0))
r=w0.sketch().segment((15,19),(16,19)).segment((16,-48)).segment((78,-48)).segment((78,74)).arc((96,92),(73,97)).segment((16,97)).segment((16,26)).segment((15,26)).close().assemble().push([(45,25)]).circle(3,mode='s').finalize().extrude(-113).union(w0.sketch().arc((16,47),(34,52),(29,34)).arc((82,87),(16,47)).assemble().finalize().extrude(59)).union(w1.workplane(offset=-147/2).moveTo(-57.5,37.5).box(85,103,147))