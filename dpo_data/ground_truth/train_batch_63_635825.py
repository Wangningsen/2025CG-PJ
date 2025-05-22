import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
r=w0.sketch().arc((-98,-29),(-87,-44),(-77,-29)).arc((-88,-10),(-98,-29)).assemble().finalize().extrude(-38).union(w0.sketch().push([(65,9)]).circle(35).push([(36,18)]).rect(10,6,mode='s').finalize().extrude(54))