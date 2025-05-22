import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,38,0))
r=w0.sketch().arc((16,-37),(13,-36),(16,-35)).arc((6,-36),(16,-37)).assemble().finalize().extrude(-138).union(w0.sketch().segment((-65,-4),(-56,-4)).segment((-56,-63)).segment((-53,-63)).segment((-53,-4)).segment((65,-4)).segment((65,63)).segment((-65,63)).close().assemble().finalize().extrude(62))