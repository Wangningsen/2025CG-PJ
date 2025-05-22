import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().segment((0,-55),(18,-55)).segment((18,-26)).arc((37,1),(18,29)).segment((18,57)).segment((0,57)).segment((0,29)).arc((-20,1),(0,-26)).close().assemble().finalize().extrude(63).union(w1.sketch().arc((-10,67),(-50,-35),(60,-45)).arc((-4,-7),(-10,67)).assemble().finalize().extrude(-100))