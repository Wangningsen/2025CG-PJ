import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
w1=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().push([(-39,-5.5)]).rect(4,77).push([(41,52.5)]).rect(6,43).finalize().extrude(-57).union(w0.sketch().push([(4,76)]).circle(24).reset().face(w0.sketch().segment((-7,66),(5,87)).segment((-7,87)).close().assemble(),mode='s').reset().face(w0.sketch().segment((3,64),(15,64)).segment((15,85)).close().assemble(),mode='s').finalize().extrude(8)).union(w1.sketch().segment((-31,15),(-31,33)).arc((-99,-10),(-19,-16)).segment((15,-16)).segment((15,15)).close().assemble().finalize().extrude(30))