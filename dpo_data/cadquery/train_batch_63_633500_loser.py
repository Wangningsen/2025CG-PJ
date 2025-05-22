import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().arc((64,-93),(71,-93),(77,-92)).segment((77,-91)).arc((73,-91),(69,-90)).arc((67,-92),(64,-93)).assemble().finalize().extrude(-77).union(w1.sketch().segment((-54,-80),(12,-80)).segment((12,-56)).arc((50,7),(12,70)).segment((12,93)).segment((-54,93)).segment((-54,70)).arc((-92,7),(-54,-56)).close().assemble().finalize().extrude(63))