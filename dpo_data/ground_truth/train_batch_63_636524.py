import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().push([(-64,44)]).circle(36).reset().face(w0.sketch().segment((34,-67),(35,-80)).segment((100,-77)).segment((99,-67)).close().assemble()).finalize().extrude(35).union(w0.sketch().arc((12,-34),(22,-39),(13,-33)).segment((13,-34)).close().assemble().push([(16,-38)]).circle(2,mode='s').finalize().extrude(82))