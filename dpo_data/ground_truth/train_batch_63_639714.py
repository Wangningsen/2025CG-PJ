import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-2))
r=w0.sketch().arc((97,16),(100,30),(97,44)).close().assemble().finalize().extrude(-10).union(w0.sketch().segment((-100,-17),(-75,-17)).arc((-35,-44),(6,-17)).segment((31,-17)).segment((31,16)).segment((6,16)).arc((-35,43),(-75,16)).segment((-100,16)).close().assemble().push([(-34.5,-22)]).rect(5,28,mode='s').finalize().extrude(15))