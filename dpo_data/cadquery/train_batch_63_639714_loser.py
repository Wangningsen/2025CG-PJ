import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-2))
r=w0.sketch().arc((97,16),(100,30),(97,44)).close().assemble().finalize().extrude(-11).union(w0.sketch().segment((-100,-17),(-75,-17)).arc((-34,-44),(6,-17)).segment((31,-17)).segment((31,16)).segment((6,16)).arc((-34,43),(-75,16)).segment((-100,16)).close().assemble().push([(-34.5,-22.5)]).rect(5,27,mode='s').finalize().extrude(14))