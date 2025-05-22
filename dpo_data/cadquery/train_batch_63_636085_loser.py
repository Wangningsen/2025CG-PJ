import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-66))
w1=cq.Workplane('XY',origin=(0,0,-62))
r=w0.sketch().arc((-65,-39),(-27,-52),(-31,-13)).arc((-85,24),(-65,-39)).assemble().reset().face(w0.sketch().segment((-86,2),(-62,-17)).segment((-46,-9)).segment((-70,14)).close().assemble(),mode='s').finalize().extrude(125).union(w1.sketch().segment((71,-30),(100,-30)).segment((100,58)).segment((71,58)).segment((71,8)).arc((65,-4),(71,-16)).close().assemble().finalize().extrude(128))