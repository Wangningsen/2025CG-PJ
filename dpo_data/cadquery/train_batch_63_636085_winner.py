import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-66))
w1=cq.Workplane('XY',origin=(0,0,-62))
r=w0.sketch().arc((-67,-39),(-28,-53),(-31,-13)).arc((-86,24),(-67,-39)).assemble().reset().face(w0.sketch().segment((-90,12),(-62,-18)).segment((-46,-9)).segment((-75,16)).segment((-73,18)).segment((-77,23)).close().assemble(),mode='s').push([(-54,-9.5)]).rect(14,5,mode='s').finalize().extrude(125).union(w1.sketch().arc((71,7),(65,-4),(72,-16)).segment((72,-30)).segment((100,-30)).segment((100,58)).segment((71,58)).close().assemble().finalize().extrude(128))