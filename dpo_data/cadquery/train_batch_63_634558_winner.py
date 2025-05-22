import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(-48,-10)]).circle(52).circle(43,mode='s').push([(45,9.5)]).rect(56,27).finalize().extrude(-55).union(w0.sketch().segment((87,-22),(100,-22)).segment((100,9)).segment((97,9)).arc((-5,26),(87,-22)).assemble().finalize().extrude(-55))