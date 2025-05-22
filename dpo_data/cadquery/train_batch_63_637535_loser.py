import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().arc((16,22),(-100,5),(17,8)).segment((100,8)).segment((100,23)).segment((16,23)).close().assemble().finalize().extrude(11).union(w0.sketch().segment((-38,-67),(-38,-65)).segment((-36,-65)).arc((-39,-62),(-38,-67)).assemble().finalize().extrude(35))