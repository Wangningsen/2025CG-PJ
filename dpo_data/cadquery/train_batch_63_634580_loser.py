import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,86))
r=w0.sketch().segment((-67,-97),(46,-100)).segment((49,-1)).arc((56,7),(61,16)).segment((60,16)).segment((67,32)).arc((50,46),(52,70)).segment((51,70)).segment((52,97)).segment((-61,100)).close().assemble().finalize().extrude(-172)