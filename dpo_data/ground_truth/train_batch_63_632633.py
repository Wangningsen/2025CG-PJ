import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().push([(-60,38)]).circle(40).push([(-53.5,23.5)]).rect(5,13,mode='s').finalize().extrude(-84).union(w0.sketch().arc((94,-63),(83,-73),(98,-72)).arc((100,-66),(94,-63)).assemble().finalize().extrude(-35))