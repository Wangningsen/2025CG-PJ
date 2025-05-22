import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-17))
r=w0.sketch().segment((-100,-60),(15,-60)).arc((87,-52),(85,19)).segment((79,70)).segment((2,60)).segment((2,44)).segment((-100,44)).close().assemble().reset().face(w0.sketch().arc((35,-26),(51,-31),(57,-16)).segment((56,-17)).arc((49,-23),(40,-23)).close().assemble(),mode='s').finalize().extrude(34)