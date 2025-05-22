import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
w1=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().push([(-39,10)]).rect(4,46).push([(41,52.5)]).rect(6,43).finalize().extrude(-58).union(w0.sketch().push([(5,76)]).circle(24).circle(11,mode='s').finalize().extrude(8)).union(w1.sketch().segment((-31,15),(-31,32)).arc((-98,-13),(-19,-16)).segment((15,-16)).segment((15,15)).close().assemble().finalize().extrude(30))